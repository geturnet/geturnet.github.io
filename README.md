# Geturnet Blog Automation Engine 🚀

[![Build Status](https://shields.io)]()
[![SEO Optimized](https://shields.io)]()
[![License](https://shields.io)]()

**Geturnet Blog Automation Engine** adalah skrip Python cerdas yang dirancang untuk menghasilkan website statis (Static Site Generation) berbasis HTML5 secara otomatis. Proyek ini memproduksi **300 artikel berkualitas tinggi yang dioptimalkan untuk SEO** (terbagi ke dalam 10 label industri, masing-masing 30 artikel unik) lengkap dengan fitur arsitektur web modern, penempatan Google AdSense secara presisi, skema validasi, serta dokumen hukum wajib.

Situs yang dihasilkan dideploy secara langsung pada platform **[Geturnet GitHub Pages](https://github.io)**.

---

## 🛠️ Fitur Utama Engine

- **300 Artikel SEO Panjang Otomatis:** Memproduksi secara massal konten informatif dengan hierarki tagHeading yang sangat terstruktur (`<h1>` sampai `<h6>`).
- **10 Label Kategori Industri:**
  - `BISNIS` & `FINANCIAL` (Edukasi Investasi, Aset Digital, & Online Commerce).
  - `PEMOGRAMAN` & `AI` (Edukasi PHP Dasar, Desain MySQL, & Prompt Engineering).
  - `LAYANAN` & `NETWORK` (Audit SEO Gratis 14 Hari, Infrastruktur Cloud, & Server Linux).
  - `TEKNOLOGI`, `KESEHATAN`, `KATA_BIJAK`, & `LOKER` (Karir IT, Lowongan Kerja WebDev, & Produktivitas).
- **Strategi Internal & External Linking:** Setiap artikel menyertakan tautan otomatis (*Terkait*) secara dinamis ke artikel lain dengan label serupa, tautan internal ke Homepage, serta tautan eksternal otoritatif (`W3C Consortium`).
- **Skema FAQ Terintegrasi:** Membantu meningkatkan peluang artikel muncul pada *Rich Snippets* di Google Search.
- **Siap Google AdSense:** Kode asinkron penempatan unit iklan (`ca-pub-4549220738609468`) sudah tersemat secara otomatis pada bagian atas dan bawah konten artikel.
- **Halaman Wajib Komplit:** Otomatis menghasilkan halaman `index.html` (Homepage), `archive.html` (Arsip Berbasis Filter), `sitemap.html` (Peta Situs Arsitektur HTML), serta `legal.html` yang memuat dokumen *Privacy Policy*, *Disclaimer*, *License Agreement*, dan *Form Kontak* klien.

---

## 📁 Struktur Repositori Proyek

```text
.
├── generate_blog.py       # Skrip generator utama Python
├── README.md              # Dokumentasi proyek (File Ini)
└── geturnet_blog/         # Direktori Output Web Statis (Siap di-Deploy)
    ├── index.html         # Halaman Utama Blog
    ├── archive.html       # Halaman Arsip Seluruh Artikel
    ├── sitemap.html       # Halaman Peta Navigasi Crawler
    ├── legal.html         # Dokumen Privasi, Lisensi, & Form Kontak
    └── [300-post-slug].html # Berkas artikel HTML5 SEO panjang
```

---

## 🚀 Cara Menjalankan Generator

### Prasyarat Sistem
Pastikan Anda telah menginstal **Python 3.x** di komputer Anda. Skrip ini dibuat murni menggunakan pustaka bawaan (*standard library*) Python (`os`, `json`, `random`, `datetime`), sehingga tidak memerlukan instalasi `pip` tambahan.

### Langkah Eksekusi

1. **Klon atau Unduh Repositori Ini:**
   ```bash
   git clone https://github.com
   cd geturnet.github.io
   ```

2. **Jalankan Skrip Generator:**
   Jalankan file `generate_blog.py` menggunakan terminal atau command prompt:
   ```bash
   python generate_blog.py
   ```

3. **Verifikasi Output:**
   Setelah proses selesai, folder `geturnet_blog` akan terisi dengan **304 file HTML**. Anda dapat membuka salah satu file (misalnya `index.html`) langsung di browser untuk melihat hasilnya.

---

## 🌐 Penyebaran (Deployment ke GitHub Pages)

Untuk mempublikasikan blog yang telah dihasilkan ke domain `https://github.io`, ikuti langkah-langkah Git berikut:

```bash
# Salin semua isi di dalam folder geturnet_blog ke root direktori repositori GitHub Pages Anda
cp -r geturnet_blog/* .

# Tambahkan file ke staging area git
git add .

# Lakukan commit perubahan dengan deskripsi berkala
git commit -m "Build: Generate 300 artikel SEO otomatis bersama Nabi Group Network"

# Unggah ke repositori GitHub utama
git push origin main
```

---

## 📋 Struktur Meta Tag SEO & AdSense yang Digunakan

Setiap halaman yang dibuat oleh generator ini secara ketat memuat standarisasi kode berikut:

* **AdSense Verification:** `<meta name="google-adsense-account" content="ca-pub-4549220738609468">`
* **AdSense Async Engine:** `<script async src="https://googlesyndication.com" crossorigin="anonymous"></script>`
* **Structured Data:** JSON-LD bertipe `Organization` dan `WebSite` untuk meningkatkan kredibilitas entitas di mata mesin pencari.
* **Social Graph:** Dilengkapi protokol `og:title`, `og:description`, `og:type`, serta `twitter:card` untuk optimalisasi ketika tautan dibagikan ke media sosial.

---

## 🏢 Kepemilikan & Jaringan Media

Situs dan teknologi automasi ini dikembangkan dan dikelola secara penuh oleh **Admin Devshel** di bawah naungan **Geturnet Ltd Group** serta didukung oleh infrastruktur distribusi **Nabi Group Network**. Konten download penunjang serta media partner yang tersemat merupakan produk resmi yang terdaftar secara legal.

---

## 📄 Lisensi

Hak Cipta Dilindungi © 2026 **Geturnet Ltd Group & Nabi Group Network**. Penggunaan komersial atau penggandaan massal terhadap konten artikel tanpa izin tertulis dari pihak manajemen dilarang keras sesuai dengan ketentuan yang tertera pada dokumen *License Agreement*.
