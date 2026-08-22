# HERAKLES World link

World linking is append-only and read-only from this repository.

Input:

- event ID and source stream;
- snapshot digest;
- receipt pointer;
- film receipt digest.

Output:

```json
{
  "schema": "herakles.film-world-link.v1",
  "filmId": "FILM-ID",
  "sourceEventId": "EVENT-ID",
  "receiptPointer": "path-or-url",
  "filmReceiptDigest": "sha256",
  "authority": "WORLD_READ_ONLY_MIRROR"
}
```

The factory never writes canonical world state and never turns an ImageGen asset into evidence.
