import os
import random
import json

# Konfigurasi Dasar
ADSENSE_CLIENT = "ca-pub-4549220738609468"
SITE_URL = "https://geturnet.github.io"
SITE_NAME = "Geturnet Ltd"

# 10 Label Utama
LABELS = [
    "Investasi", "Pemrograman", "PHP", "SEO", "Bisnis", 
    "Cloud", "FinTech", "Audit Gratis", "Teknologi", "WebDev"
]

# Template HTML Master dengan AdSense dan Komponen Lengkap
def get_html_template(title, description, content_html, label, related_links):
    return f"""<!DOCTYPE html>
<html lang="id" prefix="og: https://ogp.me/ns#">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - {SITE_NAME}</title>
    <meta name="description" content="{description}">
    <meta name="author" content="Admin {SITE_NAME}">
    <link rel="canonical" href="{SITE_URL}/">

    <!-- Google AdSense Account Verification -->
    <meta name="google-adsense-account" content="{ADSENSE_CLIENT}">

    <!-- Open Graph / Facebook Meta Tags -->
    <meta property="og:type" content="article">
    <meta property="og:url" content="{SITE_URL}/">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&auto=format&fit=crop&q=80">
    <meta property="og:site_name" content="{SITE_NAME}">
    <meta property="og:locale" content="id_ID">

    <!-- JSON-LD Structured Data (Schema.org FAQ & Article) -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "Article",
          "headline": "{title}",
          "description": "{description}",
          "author": {{
            "@type": "Organization",
            "name": "{SITE_NAME}"
          }},
          "publisher": {{
            "@type": "Organization",
            "name": "{SITE_NAME}",
            "logo": "{SITE_URL}/favicon.ico"
          }},
          "mainEntityOfPage": "{SITE_URL}/"
        }},
        {{
          "@type": "FAQPage",
          "mainEntity": [
            {{
              "@type": "Question",
              "name": "Bagaimana cara memulai topik terkait {label} bersama {SITE_NAME}?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Anda dapat mengikuti panduan mendalam dan memanfaatkan layanan profesional serta audit gratis yang disediakan oleh {SITE_NAME}."
              }}
            }},
            {{
              "@type": "Question",
              "name": "Apakah layanan yang disediakan aman dan terpercaya?",
              "acceptedAnswer": {{
                "@type": "Answer",
                "text": "Tentu, seluruh artikel dan layanan dikurasi langsung oleh tenaga ahli berpengalaman di bidangnya."
              }}
            }}
          ]
        }}
      ]
    }}
    </script>

    <!-- Google AdSense JavaScript Tag -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>

    <style>
        :root {{
            --primary-color: #007bff;
            --primary-hover: #0056b3;
            --dark-color: #222;
            --light-bg: #f4f7f6;
            --text-muted: #666;
            --border-color: #e5e5e5;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.6; background-color: var(--light-bg); color: #333; }}
        a {{ color: var(--primary-color); text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        ul {{ list-style: none; }}
        img {{ max-width: 100%; height: auto; display: block; }}
        
        .container {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
        header {{ background: #fff; border-bottom: 1px solid var(--border-color); padding: 15px 0; position: sticky; top: 0; z-index: 1000; }}
        .header-wrap {{ display: flex; justify-content: space-between; align-items: center; }}
        .logo a {{ font-size: 24px; font-weight: bold; color: var(--dark-color); }}
        nav ul {{ display: flex; gap: 20px; }}
        nav a {{ color: #555; font-weight: 500; font-size: 14px; }}

        .main-layout {{ display: grid; grid-template-columns: 1fr; gap: 30px; margin: 30px 0; }}
        @media (min-width: 768px) {{ .main-layout {{ grid-template-columns: 2fr 1fr; }} }}

        .card {{ background: #fff; padding: 25px; border-radius: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 25px; }}
        .card-title {{ font-size: 18px; margin-bottom: 15px; font-weight: bold; border-left: 4px solid var(--primary-color); padding-left: 10px; color: var(--dark-color); }}
        
        /* Typography H1-H6 Styling */
        h1 {{ font-size: 28px; margin-bottom: 15px; color: var(--dark-color); }}
        h2 {{ font-size: 22px; margin: 20px 0 10px; color: var(--dark-color); border-bottom: 2px solid var(--border-color); padding-bottom: 5px; }}
        h3 {{ font-size: 18px; margin: 15px 0 8px; color: var(--dark-color); }}
        h4, h5, h6 {{ font-size: 15px; margin: 10px 0 5px; color: #444; }}
        p {{ margin-bottom: 15px; }}

        .badge {{ background: #e1f0ff; color: var(--primary-color); padding: 3px 10px; border-radius: 4px; font-size: 12px; font-weight: bold; display: inline-block; margin-bottom: 15px; }}
        
        /* Sidebar Widgets */
        .trend-list li, .popular-list li, .archive-list li {{ padding: 10px 0; border-bottom: 1px dashed var(--border-color); font-size: 14px; }}
        .labels-flex {{ display: flex; flex-wrap: wrap; gap: 8px; }}
        .label-tag {{ background: #f0f2f5; color: #444; padding: 5px 12px; border-radius: 20px; font-size: 12px; display: inline-block; }}
        
        /* Contact Form */
        .form-group {{ margin-bottom: 15px; }}
        .form-group label {{ display: block; font-size: 13px; margin-bottom: 5px; font-weight: 500; }}
        .form-control {{ width: 100%; padding: 10px; border: 1px solid var(--border-color); border-radius: 4px; font-size: 14px; }}
        .btn-submit {{ background: var(--primary-color); color: #fff; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; font-weight: bold; width: 100%; }}
        
        .ads-placeholder {{ text-align: center; background: #e9ecef; padding: 10px; color: #6c757d; font-size: 12px; border-radius: 4px; margin: 20px 0; }}
        
        footer {{ background: #fff; border-top: 1px solid var(--border-color); padding: 40px 0 20px; margin-top: 50px; font-size: 14px; }}
        .footer-grid {{ display: grid; grid-template-columns: 1fr; gap: 30px; margin-bottom: 30px; }}
        @media (min-width: 768px) {{ .footer-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
        .footer-bottom {{ text-align: center; border-top: 1px solid var(--border-color); padding-top: 20px; color: var(--text-muted); font-size: 12px; }}
    </style>
</head>
<body>

    <header>
        <div class="container header-wrap">
            <div class="logo"><a href="{SITE_URL}/">{SITE_NAME}</a></div>
            <nav>
                <ul>
                    <li><a href="{SITE_URL}/">Home</a></li>
                    <li><a href="#related">Artikel Terkait</a></li>
                    <li><a href="#contact">Kontak</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <div class="container main-layout">
        <main>
            <div class="ads-placeholder">
                <ins class="adsbygoogle" style="display:block" data-ad-client="{ADSENSE_CLIENT}" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true"></ins>
                <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
            </div>

            <article class="card">
                <span class="badge">{label}</span>
                <h1>{title}</h1>
                <div style="font-size: 13px; color: var(--text-muted); margin-bottom: 20px;">Dipublikasikan oleh Admin {SITE_NAME} • 10 November 2026</div>
                
                <img src="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80" alt="{title}" style="border-radius: 6px; margin-bottom: 20px;">

                {content_html}

                <!-- FAQ Section -->
                <div style="margin-top: 30px; background: #f9f9f9; padding: 20px; border-radius: 6px;">
                    <h3>Pertanyaan Umum (FAQ)</h3>
                    <p><strong>Q: Bagaimana cara kerja layanan di {SITE_NAME}?</strong><br>A: Kami menyediakan panduan komprehensif serta layanan konsultasi dan audit profesional.</p>
                    <p><strong>Q: Apakah pemula dapat mengikuti panduan ini?</strong><br>A: Tentu saja, materi disusun secara bertahap dari tingkat dasar hingga mahir.</p>
                </div>

                <!-- Related Links & Download Section -->
                <div id="related" style="margin-top: 30px; border-top: 1px solid var(--border-color); padding-top: 20px;">
                    <h3>🔗 Artikel Terkait & Download Sumber Daya</h3>
                    <ul style="list-style: disc; padding-left: 20px; margin-top: 10px;">
                        {related_links}
                        <li><a href="{SITE_URL}/download-bundle.zip" download>📥 Download Source Code & Ebook Panduan ({label})</a></li>
                        <li><a href="https://github.com/geturnet" target="_blank" rel="external nofollow">🌐 Kunjungi Repository Resmi GitHub Geturnet Ltd</a></li>
                    </ul>
                </div>
            </article>

            <div class="ads-placeholder">
                <ins class="adsbygoogle" style="display:block" data-ad-client="{ADSENSE_CLIENT}" data-ad-slot="0987654321" data-ad-format="auto" data-full-width-responsive="true"></ins>
                <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
            </div>
        </main>

        <aside>
            <div class="card">
                <h2 class="card-title">🔥 Tren Terkini</h2>
                <ul class="trend-list">
                    <li><a href="#">Strategi Optimalisasi Performa Server & Web</a></li>
                    <li><a href="#">Analisis Tren FinTech & Investasi Global</a></li>
                    <li><a href="#">Update Algoritma Mesin Pencari Terbaru</a></li>
                </ul>
            </div>

            <div class="card">
                <h2 class="card-title">⭐ Postingan Populer</h2>
                <ul class="popular-list">
                    <li><a href="#">Panduan Lengkap Menguasai Pemrograman Modern</a></li>
                    <li><a href="#">Strategi Bisnis Online Skala Enterprise</a></li>
                    <li><a href="#">Audit SEO Menyeluruh untuk Trafik Organik</a></li>
                </ul>
            </div>

            <div class="card">
                <h2 class="card-title">🏷️ Label / Kategori</h2>
                <div class="labels-flex">
                    {"".join([f'<a href="#" class="label-tag">{l}</a>' for l in LABELS])}
                </div>
            </div>

            <div class="card">
                <h2 class="card-title">📅 Arsip Artikel</h2>
                <ul class="archive-list">
                    <li><a href="#">November 2026 (300 Artikel)</a></li>
                    <li><a href="#">Oktober 2026 (150 Artikel)</a></li>
                </ul>
            </div>

            <div class="card" id="contact">
                <h2 class="card-title">✉️ Hubungi Kami</h2>
                <form action="#" method="POST">
                    <div class="form-group">
                        <label>Nama Lengkap</label>
                        <input type="text" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label>Email Anda</label>
                        <input type="email" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label>Pesan / Permintaan</label>
                        <textarea class="form-control" rows="3" required></textarea>
                    </div>
                    <button type="submit" class="btn-submit">Kirim Pesan</button>
                </form>
            </div>
        </aside>
    </div>

    <footer>
        <div class="container footer-grid">
            <div>
                <h3>Tentang {SITE_NAME}</h3>
                <p style="font-size: 13px; color: var(--text-muted);">Platform edukasi terpercaya menyajikan analisis investasi, pemrograman tingkat lanjut, bisnis digital, dan optimasi SEO bersama {SITE_NAME}.</p>
            </div>
            <div>
                <h3>Tautan Navigasi</h3>
                <ul style="font-size: 13px; display: flex; flex-direction: column; gap: 6px;">
                    <li><a href="{SITE_URL}/">Beranda Utama</a></li>
                    <li><a href="#contact">Layanan Audit Gratis</a></li>
                    <li><a href="https://github.com/geturnet" target="_blank">GitHub Repository</a></li>
                </ul>
            </div>
            <div>
                <h3>Afiliasi & Partner</h3>
                <p style="font-size: 13px; color: var(--text-muted);">Didukung oleh jaringan server global dan tim engineer profesional Geturnet Group.</p>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2026 <strong>{SITE_NAME}</strong>. All Rights Reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

# Generator Konten Artikel SEO Panjang dengan H1-H6
def generate_article_content(label, index):
    title = f"Panduan Lengkap #{index}: Strategi Terbaik & Optimasi {label} Bersama Geturnet Ltd"
    description = f"Pelajari secara mendalam tentang {label.lower()} nomor {index}. Dapatkan tips eksklusif, analisis mendalam, dan layanan audit SEO gratis dari Geturnet Ltd."
    
    content_html = f"""
    <p>Selamat datang di ulasan mendalam mengenai <strong>{label}</strong> edisi ke-{index}. Di era digital yang bergerak sangat cepat saat ini, pemahaman komprehensif mengenai {label.lower()} menjadi kunci utama kesuksesan finansial maupun teknis.</p>
    
    <h2>1. Pengantar dan Urgensi {label}</h2>
    <p>Banyak praktisi seringkali mengabaikan fondasi dasar dari {label.lower()}. Padahal, dengan strategi yang tepat, efisiensi kerja dapat meningkat hingga 200%.</p>
    
    <h3>1.1 Faktor Penentu Utama</h3>
    <p>Dalam ekosistem modern, konsistensi dan penerapan teknologi mutakhir memberikan dampak langsung terhadap performa jangka panjang.</p>
    
    <h4>A. Analisis Metrik Kinerja</h4>
    <p>Melakukan evaluasi berkala memastikan setiap langkah yang diambil selaras dengan target bisnis perusahaan.</p>
    
    <h5>B. Optimalisasi Sumber Daya</h5>
    <p>Alokasi anggaran dan waktu yang terstruktur meminimalisir risiko kegagalan di tengah jalan.</p>
    
    <h6>C. Evaluasi Keamanan Sistem</h6>
    <p>Aspek keamanan tidak boleh diabaikan, terutama ketika melibatkan data pengguna atau aset digital bernilai tinggi.</p>
    
    <h2>2. Implementasi Praktis untuk Profesional</h2>
    <p>Langkah demi langkah penerapan {label.lower()} dapat langsung diintegrasikan ke dalam proyek atau portofolio investasi Anda.</p>
    
    <h3>2.1 Studi Kasus dan Hasil Nyata</h3>
    <p>Berdasarkan riset internal Geturnet Ltd, penerapan standar industri terbukti menaikkan produktivitas secara signifikan.</p>
    
    <h2>3. Kesimpulan dan Rekomendasi</h2>
    <p>Menguasai bidang {label.lower()} memerlukan dedikasi serta akses ke sumber daya yang kredibel. Manfaatkan layanan pendukung dan audit gratis dari tim kami untuk hasil optimal.</p>
    """
    return title, description, content_html

# Eksekusi Pembuatan File Otomatis (10 Label x 30 Artikel = 300 File HTML)
def main():
    print(f"Memulai pembuatan 300 artikel otomatis untuk {SITE_NAME}...")
    total_created = 0
    
    for label in LABELS:
        label_dir = label.lower().replace(" ", "-")
        os.makedirs(label_dir, exist_ok=True)
        
        for i in range(1, 31):
            title, description, content = generate_article_content(label, i)
            
            # Buat link internal acak tiruan
            related_links = f"""
                <li><a href="{SITE_URL}/{label_dir}/artikel-{random.randint(1,30)}.html">Baca Juga: Panduan Lanjutan {label} Part {random.randint(1,30)}</a></li>
                <li><a href="{SITE_URL}/investasi/artikel-1.html">Eksplorasi Topik Finansial & Investasi Terkait</a></li>
            """
            
            html_code = get_html_template(title, description, content, label, related_links)
            
            filename = f"{label_dir}/artikel-{i}.html"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(html_code)
            
            total_created += 1

    print(f"Sukses! Berhasil men-generate {total_created} file artikel lengkap dengan AdSense, Schema FAQ, dan struktur H1-H6.")

if __name__ == "__main__":
    main()
