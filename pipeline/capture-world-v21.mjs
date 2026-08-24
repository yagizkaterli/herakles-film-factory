#!/usr/bin/env node
// Read-only HERAKLES WORLD v21 capture for the Film Factory.
// It never forwards commands and never serializes raw thoughts or secrets.

import fs from 'node:fs/promises';
import path from 'node:path';

function arg(name, fallback) {
  const i = process.argv.indexOf(name);
  return i >= 0 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
}

const base = (arg('--base-url', 'http://127.0.0.1:3419')).replace(/\/$/, '');
const durationMs = Number(arg('--duration-ms', '12000'));
const output = arg('--out', 'iterations/world-v21-live-capture.json');

const safeAgent = (a) => ({
  id: a?.id ?? null,
  model: a?.model ?? null,
  status: a?.status ?? null,
  restarts: Number.isFinite(a?.restarts) ? a.restarts : 0,
});

const safeEvent = (row) => {
  const e = row?.event ?? {};
  return {
    seq: row?.seq ?? null,
    ts: row?.ts ?? null,
    type: e.type ?? e.eventType ?? null,
    id: e.id ?? e.eventId ?? null,
    agentId: e.agentId ?? e.agent_id ?? null,
    taskId: e.taskId ?? e.task_id ?? null,
    status: e.status ?? null,
    tool: e.tool ?? e.toolName ?? null,
    receiptId: e.receiptId ?? e.receipt_id ?? null,
  };
};

async function getJson(path) {
  const response = await fetch(`${base}${path}`, { signal: AbortSignal.timeout(5000) });
  if (!response.ok) throw new Error(`${path} HTTP ${response.status}`);
  return response.json();
}

const status = await getJson('/status');
const raw = await getJson('/v2/snapshot');
const snapshot = raw.snapshot ?? raw;
const domains = snapshot.domains ?? {};
const agents = Array.isArray(domains.agents) ? domains.agents : (domains.agents?.liste ?? []);
const capture = {
  schema: 'herakles.world-v21-film-capture.v1',
  capturedAt: new Date().toISOString(),
  source: { base, relay: status.schemaVersion, snapshotId: snapshot.snapshotId, createdAt: snapshot.createdAt },
  relay: {
    cursor: status.cursor ?? 0,
    recentEvents: status.recentEvents ?? 0,
    hasSnapshot: Boolean(status.hasSnapshot),
    snapshotDigest: status.snapshotDigest ?? null,
  },
  agents: agents.map(safeAgent),
  aggregates: {
    agentCount: agents.length,
    working: agents.filter((a) => a.status === 'working' || a.status === 'running').length,
    idle: agents.filter((a) => a.status === 'idle').length,
    taskCount: Array.isArray(domains.tasks) ? domains.tasks.length : (domains.tasks?.liste?.length ?? null),
  },
  events: [],
  privacy: { rawThoughts: false, encryptedReasoning: false, credentials: false, commandsSent: false },
};

const controller = new AbortController();
const timer = setTimeout(() => controller.abort(), durationMs);
try {
  const response = await fetch(`${base}/events?cursor=${capture.relay.cursor}`, {
    headers: { Accept: 'text/event-stream' }, signal: controller.signal,
  });
  if (!response.ok || !response.body) throw new Error(`/events HTTP ${response.status}`);
  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = '';
  while (true) {
    const { value, done } = await reader.read();
    if (done) break;
    buffer += decoder.decode(value, { stream: true });
    const chunks = buffer.split('\n\n');
    buffer = chunks.pop() ?? '';
    for (const chunk of chunks) {
      const data = chunk.split('\n').find((line) => line.startsWith('data: '));
      if (!data) continue;
      try { capture.events.push(safeEvent(JSON.parse(data.slice(6)))); } catch {}
    }
  }
} catch (error) {
  capture.eventsError = error.name === 'AbortError' ? null : String(error.message ?? error);
} finally {
  clearTimeout(timer);
}

await fs.mkdir(path.dirname(output), { recursive: true });
await fs.writeFile(output, `${JSON.stringify(capture, null, 2)}\n`, 'utf8');
console.log(JSON.stringify({ output, snapshotId: capture.source.snapshotId, events: capture.events.length, commandsSent: false }));
