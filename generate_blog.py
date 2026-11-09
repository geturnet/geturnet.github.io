# 3. Pembuatan Struktur Artikel Otomatis Berbasis SEO (Skema Internal Linking Mutakhir)
print("Memulai pembuatan 300 artikel dengan Skema Internal Linking Kontekstual...")
for idx, current_post in enumerate(all_posts):
    
    # A. Tautan Navigasi Sequence (Next - Previous Article)
    prev_post = all_posts[idx - 1] if idx > 0 else all_posts[-1]
    next_post = all_posts[idx + 1] if idx < len(all_posts) - 1 else all_posts[0]
    
    sequence_links_html = f'''
    <div style="display: flex; justify-content: space-between; gap: 15px; margin: 20px 0; padding: 10px; background: #f8f9fa; border-radius: 6px; font-size: 13px;">
        <div>&larr; <strong>Sebelumnya:</strong> <a href="{SITE_URL}{prev_post['slug']}">{prev_post['title']}</a></div>
        <div style="text-align: right;"><strong>Selanjutnya:</strong> <a href="{SITE_URL}{next_post['slug']}">{next_post['title']}</a> &rarr;</div>
    </div>
    '''

    # B. Tautan Kontekstual Berdasarkan Relasi Label (Related Posts Berbasis Silo Kategori)
    related_posts = [p for p in all_posts if p['label'] == current_post['label'] and p['id'] != current_post['id']][:3]
    
    related_links_html = "<ul class='archive-list'>"
    for rp in related_posts:
        related_links_html += f'<li><a href="{SITE_URL}{rp["slug"]}">{rp["title"]}</a></li>'
    related_links_html += "</ul>"

    # C. Tautan Silang Kontekstual ke Label Kategori Lain (Cross-Linking Antar Silo)
    # Mencari label alternatif untuk menjaga interlink antar kategori tetap hidup
    other_labels = [l for l in labels_data.keys() if l != current_post['label']]
    cross_label_1 = other_labels[idx % len(other_labels)]
    cross_label_2 = other_labels[(idx + 1) % len(other_labels)]
    
    cross_post_1 = random.choice([p for p in all_posts if p['label'] == cross_label_1])
    cross_post_2 = random.choice([p for p in all_posts if p['label'] == cross_label_2])

    # Pembentukan Teks HTML Konten SEO dengan Injeksi Internal Link di Setiap Paragraf
    content_html = f'''
    <article class="article-body">
        <span class="badge">{current_post['label']}</span>
        <h1>{current_post['title']}</h1>
        <div class="meta-text">Dipublikasikan oleh {current_post['author']} pada {current_post['date']} | Kategori: <a href="{SITE_URL}archive.html?label={current_post['label']}">{current_post['label']}</a></div>
        
        <p>Selamat datang di platform **Geturnet Ltd Group**. Artikel khusus ini menyajikan pembahasan mendalam mengenai topik <strong>{current_post['title']}</strong> yang dirancang khusus untuk memenuhi standar optimasi search engine modern, berkolaborasi dalam jaringan infrastruktur <a href="{SITE_URL}index.html">Halaman Utama Geturnet</a>.</p>
        
        <h2>Mengapa Struktur {current_post['label']} Begitu Penting?</h2>
        <p>Dalam ekosistem digital saat ini, optimasi yang dilakukan oleh sistem backend Geturnet membantu para profesional menemukan solusi operasional terbaik. Seringkali, integrasi ini berkaitan erat dengan penemuan baru di kategori lain seperti artikel rekomendasi kami tentang <a href="{SITE_URL}{cross_post_1['slug']}">{cross_post_1['title']}</a> yang terbukti mendongkrak efisiensi kerja kerja hingga level maksimal.</p>
        
        <h3>Analisis Komponen Struktural Utama</h3>
        <p>Berdasarkan cetak biru teknologi terbaru, kami membagi elemen fundamental ini menjadi beberapa sub-metodologi operasional terukur. Untuk komparasi data finansial yang relevan, Anda juga dipersilakan meninjau rilis sistem bertajuk <a href="{SITE_URL}{cross_post_2['slug']}">{cross_post_2['title']}</a> guna memperluas wawasan arsitektur Anda.</p>
        
        <h4>Penerapan Praktis Skema Kerja Lapangan</h4>
        <p>Langkah implementasi operasional dapat dipelajari secara bertahap melalui sistem integrasi repositori internal kami yang dapat diakses langsung via navigasi <a href="{SITE_URL}archive.html">Arsip Data Terstruktur Blog</a>.</p>
        
        <h5>Catatan Teknis Tambahan Developer</h5>
        <p>Pastikan konfigurasi lingkungan kerja Anda selaras dengan regulasi komputasi awan Geturnet Global dan lisensi penggunaan data bersama.</p>
        
        <h6>Metode Evaluasi Akhir (H6 Tag)</h6>
        <p>Prosedur pengujian akhir wajib dilakukan untuk meminimalisir kegagalan beban kerja sistem.</p>
        
        <h2>Tautan Navigasi Referensi Industri (Link Eksternal Otoritatif)</h2>
        <p>Untuk eksplorasi materi standar industri berskala internasional, Anda dapat memeriksa standar protokol industri di dunia luar melalui tautan eksternal otoritatif berikut: <a href="https://w3.org" target="_blank" rel="noopener noreferrer">W3C Official Consortium</a>.</p>
        
        {sequence_links_html}

        <h2>Artikel Terkait Sejenis (Silo Kategori {current_post['label']})</h2>
        <div class="card" style="background:#f8f9fa; border-left: 4px solid var(--primary-color);">
            {related_links_html}
        </div>

        <div class="faq-section">
            <h2 style="font-size:20px; margin-top:0;">Frequently Asked Questions (FAQ)</h2>
            <div class="faq-item">
                <div class="faq-q">Q: Apakah Layanan Audit SEO Geturnet benar-benar gratis?</div>
                <div class="faq-content">A: Ya, Geturnet Ltd memberikan masa uji coba penuh gratis selama 14 hari tanpa dipungut biaya operasional apa pun.</div>
            </div>
            <div class="faq-item">
                <div class="faq-q">Q: Di mana saya bisa menemukan rangkuman tautan sitemap?</div>
                <div class="faq-content">A: Indeks lengkap seluruh file telah kami petakan secara berkala pada halaman khusus <a href="{SITE_URL}sitemap.html">Indeks Peta Situs HTML Geturnet</a>.</div>
            </div>
        </div>
    </article>
    '''
    
    # Generate Output File Artikel
    rendered_html = get_html_template(current_post['title'], content_html, current_page="home")
    with open(os.path.join(BASE_DIR, current_post['slug']), "w", encoding="utf-8") as f:
        f.write(rendered_html)
