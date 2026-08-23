kart: d-FILM-ANLATI-02-label-vs-stream.md
kanal: oda
ajan: 12
ajan_kanali: codex
gecen_sure: 4m47.323s
kart_yolu: /root/vault-homebase/02 Projects/Sistem-Insa/gorevler/_oda-kuyruk/sistem-analizi-s106/islenen/d-FILM-ANLATI-02-label-vs-stream.md
sonuc: basarili

{
  "kart": "d-FILM-ANLATI-02-label-vs-stream.md",
  "kart_yolu": "/root/vault-homebase/02 Projects/Sistem-Insa/gorevler/_oda-kuyruk/sistem-analizi-s106/islenen/d-FILM-ANLATI-02-label-vs-stream.md",
  "durum": "tamamlandi_adayi",
  "sonuc": "Tek source-bound deterministic scene JSON'u uretildi; tek hamle yesil kosuyor etiketini donmus akis kuyrugu ile celistiriyor.",
  "makbuzlar": {
    "kart_okuma": {
      "komut": "sed -n '1,240p' '/root/vault-homebase/02 Projects/Sistem-Insa/gorevler/_oda-kuyruk/sistem-analizi-s106/islenen/d-FILM-ANLATI-02-label-vs-stream.md'",
      "cikti": "kart mevcut; canonical/label-is-not-evidence.v1.json; single move label-versus-stream; JSON receipt ve Markdown olmayan cikti istendi.",
      "olcum": "card bytes=730"
    },
    "canonical": {
      "path": "/root/vault-homebase/02 Projects/Sistem-Insa/canonical/label-is-not-evidence.v1.json",
      "test_f": 0,
      "bytes": 691,
      "lines": 12,
      "sha256": "c0c55f2a0bfadfa6cb5f88c79f5b3b17b4c041972dec08cad13f76b0fdf9dbea",
      "json_parse": "OK",
      "komut": "test -f; wc -c; wc -l; sha256sum; jq -e .",
      "cikti": "test_f=0 bytes=691 lines=12 sha256=c0c55f2a0bfadfa6cb5f88c79f5b3b17b4c041972dec08cad13f76b0fdf9dbea json=OK"
    },
    "canonical_alanlari": {
      "id": "label-is-not-evidence",
      "single_move": "label-versus-stream",
      "room_source": "de2b53bf-a6a6-459b-a393-b30210d6fb46",
      "fake_evidence": false,
      "measured_instance": "2c0b22e4 dosya-mtime'inda CANLI gorunuyordu; akisinin son satiri 23 Agu 02:14'ten beri model=<synthetic> output_tokens=0. Etiket kosuyor dedi, akis park etmis dedi.",
      "makbuz": "jq -r .id,.single_move,.room_source,.fake_evidence,.measured_instance canonical/label-is-not-evidence.v1.json"
    },
    "oda_kaynagi": {
      "path": "/root/vault-homebase/02 Projects/Sistem-Insa/gorevler/_durum/hterm-durum.json",
      "test_f": 0,
      "bytes": 192053,
      "lines": 3577,
      "sha256": "a15670e51a4afd23a482f938eac755553f4db1e30213d4796586f29fc9be684a",
      "json_parse": "OK",
      "room_id": "de2b53bf-a6a6-459b-a393-b30210d6fb46",
      "room_match_count": 1,
      "room_name": "HERAKLES Film Factory ImageGen + Manim + HERAKLES World kanitli film uretim hatti",
      "room_role": "member",
      "room_pending_offer_count": 1,
      "komut": "jq --arg id de2b53bf-a6a6-459b-a393-b30210d6fb46 '[.odalar[] | select(.id==$id)] | length'; jq oda kaydini okudu",
      "cikti": "room_match_count=1 room_ad=HERAKLES Film Factory ImageGen + Manim + HERAKLES World kanitli film uretim hatti room_role=member room_pending_offer_count=1"
    },
    "oda_olcumu": {
      "kapsam": "hterm-durum.json genel olcum alani; room-specific degil",
      "deger": {
        "load1": 12.37,
        "ajan": 5,
        "failed": 0,
        "m7_kayit": 2161,
        "bild_bekleyen": 663
      },
      "komut": "jq -c .olcum /root/vault-homebase/02 Projects/Sistem-Insa/gorevler/_durum/hterm-durum.json",
      "cikti": "{\"load1\":12.37,\"ajan\":5,\"failed\":0,\"m7_kayit\":2161,\"bild_bekleyen\":663}"
    },
    "stream_token_arama": {
      "aranan": "2c0b22e4",
      "kapsam": "/root/vault-homebase/02 Projects/Sistem-Insa; readable files; claim-run ve is-durumu dosyalari disarida",
      "komut": "rg -n -F --hidden --glob '!**/.git/**' --glob '!**/claim-run-*.md' --glob '!**/*.is-durumu.json' '2c0b22e4' '/root/vault-homebase/02 Projects/Sistem-Insa' | wc -l",
      "cikti": "item_id_occurrences_in_readable_sistem-insa=1",
      "sinir": "Bagimsiz transcript/stream dosyasi icin ayri path makbuzu yok; stream tail yalniz kanonik measured_instance alanindan kullanildi."
    },
    "path_farki": {
      "karttaki_aday": "canonical/label-is-not-evidence.v1.json",
      "olculen": "/root/vault-homebase/02 Projects/Sistem-Insa/canonical/label-is-not-evidence.v1.json",
      "sonuc": "fark_yok",
      "makbuz": "test_f=0; jq parse=OK; sha256=c0c55f2a0bfadfa6cb5f88c79f5b3b17b4c041972dec08cad13f76b0fdf9dbea"
    }
  },
  "scene": {
    "path": "/root/vault-homebase/02 Projects/Sistem-Insa/gorevler/_oda-kuyruk/sistem-analizi-s106/islenen/d-FILM-ANLATI-02-label-vs-stream.scene.json",
    "sha256": "efaa7d78985b538d66b6fc4467fd1bb7ab5917521b180a8b2bbd8bfe146e89cc",
    "bytes": 2600,
    "lines": 64,
    "deterministic": true,
    "single_move_count": 1,
    "beat_count": 3,
    "binding_count": 3,
    "invented_evidence": false,
    "makbuz": {
      "komut": "jq -e . scene.json; jq -e scene contract; wc -c; wc -l; sha256sum",
      "cikti": "scene_test_f=0 bytes=2600 lines=64 sha256=efaa7d78985b538d66b6fc4467fd1bb7ab5917521b180a8b2bbd8bfe146e89cc; scene_json=OK; scene_contract=PASS; single_move_count=1 beat_count=3 binding_count=3; source_paths_test_f=0 room_id_match=1"
    }
  },
  "qa": {
    "json": "PASS",
    "ascii_only": "PASS",
    "single_move": "PASS",
    "source_binding": "PASS",
    "falsifier": "Park etmis panel gercek bir transkriptteki sentetik son-satira baglanamazsa sahne REDDEDILIR.",
    "makbuz": "jq -e scene contract exit=0; LC_ALL=C grep -nP '[^\\x00-\\x7F]' scene.json -> no output; source_paths_test_f=0; room_id_match=1"
  },
  "olculmeyen": [
    "Ayrica bir transcript dosyasinin 2c0b22e4 son satirini bagimsiz olarak tasidigi olculmedi.",
    "Render komutu, PNG veya MP4 olculmedi; kart JSON receipt istedi, bu tur cikti scene JSON ile sinirlandi.",
    "Kanonik measured_instance disinda yeni zaman, model veya output satiri uydurulmadi."
  ],
  "UYE-FIKRI": {
    "GOZLEM": "Yesil kosuyor etiketi, ayni kanonik measured_instance icindeki 23 Agu 02:14'ten beri model=<synthetic> output_tokens=0 kuyrugu ile tek hamlede celistirilebilir; oda kaynagi da kanonik room_source ile birebir eslesti.",
    "DAYANAK": "canonical sha256=c0c55f2a0bfadfa6cb5f88c79f5b3b17b4c041972dec08cad13f76b0fdf9dbea; hterm sha256=a15670e51a4afd23a482f938eac755553f4db1e30213d4796586f29fc9be684a; room_match_count=1; scene_contract=PASS; single_move_count=1.",
    "ONERME": "Film sahnesi label durumunu tek basina kanit saymasin; stream tail ayni kaynak makbuzuna baglanmadan contradiction hold kurulmasin.",
    "TERS-ORNEK": "Ayni room_source icin bagimsiz canli transcript makbuzu, 23 Agu 02:14 sonrasi yeni stream satiri ve output_tokens sifir olmayan devam kaniti bulunursa bu sahnedeki donmus kuyruk gozlemi curur.",
    "KOSTUGU IS": "Kart, canonical JSON, hterm oda kaydi ve genel olcum okundu; canonical ve hterm hashleri alindi; room ID tek eslesme olarak sayildi; tek hamleli source-bound scene JSON yazildi; JSON, ASCII, kaynak baglama ve tek hamle kontrolleri kosuldu."
  }
}
