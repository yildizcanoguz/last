# Birim Fiyat Arama (GitHub Pages)

Bu repo, `Data base Pricing.xlsx` dosyasındaki birim fiyatları **tarayıcıda** aramak/filtrelemek için hazırlanmış basit bir web uygulamasıdır.

## Özellikler
- ART / Açıklama / Seri / Kategori / UM üzerinde arama
- Seri, Kategori, UM filtreleri
- Sıralama (ART, DZD, Euro)
- Satır detay ekranı + panoya kopyalama
- Seçilen kalemleri CSV export

## GitHub Pages ile yayınlama
1. Bu repo’yu GitHub’a yükle.
2. **Settings → Pages**
3. **Build and deployment → Source: Deploy from a branch**
4. Branch: `main` / Folder: `/ (root)`
5. Kaydet → sayfa `https://<kullanici>.github.io/<repo>/` adresinde açılır.

## Veri güncelleme
Yeni Excel gelirse `pricing.json` dosyasını yeniden üretmen yeterli.

Aşağıdaki script’i kullanabilirsin (opsiyonel):
- `build_data.py` dosyasını çalıştır
- ürettiği `pricing.json`’u repoya koy

> Not: GitHub Pages’te `fetch("./pricing.json")` çalışması için dosya aynı klasörde olmalı.
