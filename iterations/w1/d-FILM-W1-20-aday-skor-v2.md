---
kanal: oda
dokunur: evet
gerektirir: [oku, kos, yaz]
sinif: 4
aile: aracli
---
# W1 film aday skoru — karar atomu görevi

Yalnızca geçerli `karar-atomu-v1` JSON döndür. Beş alan zorunlu: `soru`, `secenek`, `kanit`, `durum`, `makbuz`. Ek alan ekleme.

W1 I01-I20 adaylarını `iterations/w1/W1-MANIFEST.json` ve ImageGen referansı `iterations/w1/concept-01-evidence-thread.png` üzerinden değerlendir. HERAKLES paper, 3B1B anlatı ve motion contract ilkelerini kullan. ImageGen kanıt değildir.

`kanit` alanı içinde kaçışlanmış JSON olarak şu yapıyı ver: `{ "schema":"herakles.w1-score.v1", "scores":[{"id":"I01","audience_clarity":0,"causal_legibility":0,"source_parity":0,"object_continuity":0,"world_authority":0,"craft":0,"total":0,"decision":"keep|reject","falsifier":"..."}], "top10":["..."] }`. Her puan 0-1 arası olmalı; toplam canonical ağırlıklarla hesaplanmalı; >=0.82 yalnızca keep olabilir. Kaynak pointeri yoksa source_parity=0 ve reject.

`durum` W1’in sonucu, `makbuz` kullanılan kaynaklar ve hesap yöntemi olsun. Markdown raporu üretme; yalnızca JSON.
