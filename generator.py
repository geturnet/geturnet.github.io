#!/usr/bin/env python3
"""Generator for Geturnet static SEO pages.

This script creates a GitHub Pages-ready site structure for Geturnet Ltd,
including category pages, legal pages, regional pages, a homepage, sitemap,
and article pages with SEO metadata, schema.org JSON-LD, FAQ, table of contents,
and internal/external link blocks.

Usage:
    python generator.py
    python generator.py --articles-per-category 3 --output .
    python generator.py --articles-per-category 5 --min-words 3000
"""

from __future__ import annotations

import argparse
import html
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import quote

SITE_URL = "https://geturnet.github.io"
SITE_NAME = "Geturnet Ltd"
ADSENSE_CLIENT = "ca-pub-4549220738609468"
DEFAULT_ARTICLES_PER_CATEGORY = 2
MIN_WORDS = 3000

CATEGORIES = {
    "investasi": "Investasi",
    "bisnis": "Bisnis",
    "teknologi": "Teknologi",
    "tech": "Tech",
    "health": "Health",
    "news": "News",
    "pemrograman": "Pemrograman",
    "php": "PHP",
    "seo": "SEO",
    "cloud": "Cloud",
    "fintech": "FinTech",
    "webdev": "Web Development",
}

REGIONS = [
    "Jakarta", "Jawa Barat", "Jawa Timur", "Jawa Tengah", "Sumatera Utara",
    "Banten", "Sulawesi Selatan", "Bali", "Sumatera Selatan", "Yogyakarta",
    "Riau", "Lampung", "Kalimantan Timur", "Kalimantan Barat", "Sumatera Barat",
    "Bogor", "Bekasi", "Malang", "Surakarta", "Batam",
]

LEGAL_PAGES = {
    "about-us": ("About Us", "Tentang Kami"),
    "contact-us": ("Contact Us", "Hubungi Kami"),
    "sitemap": ("Sitemap", "Sitemap"),
    "disclaimer": ("Disclaimer", "Disclaimer"),
    "privacy-policy": ("Privacy Policy", "Kebijakan Privasi"),
    "terms": ("Terms and Conditions", "Syarat dan Ketentuan"),
    "license": ("License", "Lisensi"),
    "join-forum": ("Join Forum", "Forum"),
    "pedoman-siber": ("Pedoman Siber", "Pedoman Siber"),
    "cookies": ("Cookies", "Kebijakan Cookies"),
}

EXTERNAL_LINKS = {
    "investasi": [
        ("OJK", "https://www.ojk.go.id/"),
        ("Bank Indonesia", "https://www.bi.go.id/"),
        ("Bursa Efek Indonesia", "https://www.idx.co.id/"),
        ("Kementerian Keuangan RI", "https://www.kemenkeu.go.id/"),
        ("Sikapi Uangmu", "https://sikapiuangmu.ojk.go.id/"),
        ("BPS", "https://www.bps.go.id/"),
        ("Investopedia", "https://www.investopedia.com/"),
    ],
    "health": [
        ("Kemenkes RI", "https://www.kemkes.go.id/"),
        ("WHO", "https://www.who.int/"),
        ("MedlinePlus", "https://medlineplus.gov/"),
        ("Cleveland Clinic", "https://my.clevelandclinic.org/health"),
        ("NHS", "https://www.nhs.uk/conditions/"),
        ("Badan POM RI", "https://www.pom.go.id/"),
        ("PubMed", "https://pubmed.ncbi.nlm.nih.gov/"),
    ],
    "tech": [
        ("Komdigi", "https://www.komdigi.go.id/"),
        ("BSSN", "https://www.bssn.go.id/"),
        ("W3C", "https://www.w3.org/"),
        ("MDN", "https://developer.mozilla.org/"),
        ("Google Search Central", "https://developers.google.com/search/docs"),
        ("OWASP", "https://owasp.org/"),
        ("NIST", "https://www.nist.gov/"),
    ],
    "default": [
        ("Komdigi", "https://www.komdigi.go.id/"),
        ("BPS", "https://www.bps.go.id/"),
        ("Google Search Central", "https://developers.google.com/search/docs"),
        ("W3C", "https://www.w3.org/"),
        ("OJK", "https://www.ojk.go.id/"),
        ("WHO", "https://www.who.int/"),
        ("OWASP", "https://owasp.org/"),
    ],
}


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "artikel"


def article_path(category_slug: str, article_slug: str, year: str, month: str) -> str:
    return f"{category_slug}/{year}/{month}/{article_slug}.html"


def make_article_intro(label: str, index: int, topic: str, year: str, month: str) -> dict:
    title = f"Panduan Lengkap #{index}: {topic} {label} untuk Strategi Digital, Keputusan, dan Growth yang Lebih Kuat"
    description = (
        f"Pelajari {topic.lower()} {label.lower()} secara mendalam, mulai dari dasar, strategi, eksekusi, hingga hasil yang dapat diukur. "
        f"Artikel ini disusun untuk pembaca Indonesia yang ingin memahami tren, tools, dan praktik terbaik di {label.lower()}."
    )
    return {
        "title": title,
        "slug": slugify(f"{label}-{topic}-{index}"),
        "description": description,
        "category": label,
        "category_slug": slugify(label),
        "date": f"{year}-{month}-01",
        "year": year,
        "month": month,
    }


def render_section(heading: str, paragraphs: list[str]) -> str:
    body = [f"<h2>{esc(heading)}</h2>"]
    for p in paragraphs:
        body.append(f"<p>{esc(p)}</p>")
    return "\n".join(body)


def build_article_body(label: str, topic: str, index: int, related_links: list[str], shared_internal_links: list[str]) -> str:
    section_titles = [
        "Pengantar dan urgensi topik",
        "Dasar pemahaman dan definisi",
        "Konteks pasar dan tren Indonesia",
        "Strategi eksekusi yang tepat",
        "Tabel KPI, prioritas, dan checklist",
        "Risiko, hambatan, dan mitigasi",
        "Implementasi praktis untuk tim dan individu",
        "Pertanyaan umum dan jawaban cepat",
        "Kesimpulan dan langkah berikutnya",
    ]

    # Generate a long article with 3000+ words by repeating rich paragraphs and examples.
    paragraphs_by_section = {
        "Pengantar dan urgensi topik": [
            f"{label} terus berkembang dalam ekosistem digital Indonesia. Saat pembaca mencari solusi yang relevan, kebutuhan akan informasi yang akurat, praktis, dan terukur menjadi penting. Dalam konteks {topic.lower()}, keberhasilan tidak hanya ditentukan oleh pengetahuan umum, tetapi juga oleh disiplin dalam mengelola eksekusi, evaluasi, dan optimasi. {label} bukan sekadar istilah populer; ia juga mewakili cara berpikir yang dapat membantu individu, bisnis, dan organisasi menciptakan keputusan yang lebih konsisten.",
            f"Pada tahun 2026, kebutuhan akan pemahaman serius terhadap {label.lower()} makin meningkat karena pasar, konsumen, serta ekosistem teknologi berubah lebih cepat dari sebelumnya. Banyak organisasi berupaya menyesuaikan model kerja mereka agar tetap relevan, namun tidak semua strategi dijalankan dengan pendekatan yang tepat. Oleh karena itu, artikel ini hadir untuk memberikan kerangka yang dapat dibaca secara bertahap, mulai dari dasar, tren, sampai cara mengimplementasikan strategi yang setara dengan kebutuhan pasar modern.",
            f"Perlu dipahami bahwa {label.lower()} tidak bisa dinilai hanya dari satu metrik. Keberhasilan sering kali tergantung pada interaksi antara strategi, analisis data, konsistensi, dan kemampuan menilai konteks. Dalam dunia profesional yang penuh tekanan, pendekatan yang terlalu umum sering gagal karena tidak menghubungkan teori dengan kebutuhan operasional. Karena itu, artikel ini menggabungkan konteks, praktik, dan referensi yang relevan agar keputusan menjadi lebih akurat.",
        ],
        "Dasar pemahaman dan definisi": [
            f"Biasanya, pembahasan tentang {label.lower()} dimulai dari pemahaman terminologi dan kerangka kerja. Definisi yang jelas akan membantu pembaca membedakan antara praktik yang benar dan klaim yang hanya bersifat promosi. Dalam banyak industri, pemahaman yang dangkal justru menimbulkan keputusan yang merugikan, terutama ketika konsekuensi strategi tidak dipertimbangkan dengan matang.",
            f"Untuk membangun fondasi, penting melihat {label.lower()} sebagai sistem yang saling terhubung: input, proses, output, dan evaluasi. Ketika salah satu elemen lemah, hasil yang keluar juga dipengaruhi. Misalnya, tim yang memiliki data lengkap tetapi tidak memahami prioritas akan menghabiskan waktu pada aktivitas yang tidak berdampak besar. Di sisi lain, tim yang memiliki gagasan kuat tanpa evaluasi dan feedback yang konsisten juga akan kesulitan dalam mempertahankan eksekusi.",
            f"Karena itu, pemahaman {label.lower()} harus didukung oleh tiga prinsip utama: kejelasan tujuan, keterukuran, dan mekanisme perbaikan berkelanjutan. Kejelasan tujuan menyusun prioritas. Keterukuran memastikan data valid. Mekanisme perbaikan berkelanjutan menjaga agar organisasi tidak stagnan. Prinsip-prinsip ini tidak hanya berlaku untuk perusahaan besar, tetapi juga untuk pelaku usaha kecil, creator, serta profesional individu.",
            f"Kriteria kualitas juga perlu diperhatikan. Artikel yang bagus tidak hanya menjelaskan konsep, tetapi juga menyampaikan kondisi penerapan nyata, tren, dan konsekuensi jika tidak ada disiplin. Jadi, pembaca tidak hanya menerima penjelasan umum, melainkan juga alat untuk mengevaluasi keputusan mereka secara lebih kritis.",
        ],
        "Konteks pasar dan tren Indonesia": [
            f"Di Indonesia, {label.lower()} sangat berkaitan dengan perubahan perilaku digital, kebutuhan akan efisiensi, dan tuntutan agar keputusan makin berbasis data. Konsumen kini lebih sadar terhadap kualitas informasi, sehingga merek yang menonjol adalah mereka yang konsisten, relevan, dan terbuka terhadap pembaruan. Dalam konteks ini, {topic.lower()} berperan sebagai jembatan antara kebutuhan pasar dan kemampuan organisasi untuk menyesuaikan model kerja.",
            f"Banyak perusahaan mulai mengadopsi pendekatan yang lebih terstruktur, terutama ketika ekosistem digital semakin kompleks. Tren yang terlihat adalah meningkatnya kebutuhan terhadap data yang terorganisir, pengelolaan komunikasi yang lebih jelas, serta sistem evaluasi yang dapat diakses oleh tim lintas fungsi. Semua ini penting agar keputusan tidak terlalu didasarkan pada asumsi atau tekanan sesaat.",
            f"Penyebaran informasi juga memengaruhi cara audiens berinteraksi dengan topik {label.lower()}. Mereka tidak lagi puas dengan isi yang terlalu umum atau terlalu panjang tanpa substansi. Mereka membutuhkan informasi yang memiliki struktur, bukti, dan relevansi yang jelas. Dengan demikian, editor, content strategist, atau profesional yang ingin membangun reputasi harus menempatkan kualitas, keakuratan, dan pembaruan sebagai pilar utama.",
            f"Di sisi bisnis, tren ini memunculkan peluang besar untuk membuat konten, produk, dan layanan yang lebih relevan. Namun, peluang akan berubah menjadi risiko jika eksekusi tidak disiapkan dengan matang. Oleh karena itu, memahami konteks pasar bukan hanya soal mengikuti tren, tetapi juga mengukur apakah tren tersebut relevan dengan kebutuhan pembaca, konsumen, dan strategi organisasi.",
        ],
        "Strategi eksekusi yang tepat": [
            f"Setelah memahami dasar, langkah berikutnya adalah eksekusi. Strategi {label.lower()} yang efektif dibangun dengan tiga tahap: analisis kebutuhan, prioritasi, dan evaluasi ulang. Tahap pertama memastikan pertanyaan yang ingin dijawab sangat jelas. Tahap kedua memastikan sumber daya dialokasikan dengan benar. Tahap ketiga memastikan instrumen evaluasi berjalan dengan baik untuk mengukur hasil.",
            f"Dalam praktiknya, tim sering gagal bukan karena ide tidak bagus, tetapi karena proses eksekusi tidak terdokumentasi dengan jelas. Oleh sebab itu, rutinitas evaluasi mingguan, checklist, dan pemetaan tanggung jawab adalah elemen yang sangat penting. Pada saat yang sama, tidak semua alat harus dipakai sekaligus. Menggunakan terlalu banyak tool secara bersamaan dapat membingungkan tim dan mengurangi fokus.",
            f"Prinsip terbaik adalah mulai dengan kebutuhan yang paling berpengaruh dan buat jalur kerja yang bisa diperiksa secara berkala. Misalnya, organisasi dapat memulai dari segmentasi audiens, identifikasi masalah utama, lalu mengukur efektivitas tertentu sebelum memperluas strategi. Pendekatan ini mengurangi risiko dan memberi ruang bagi iterasi yang lebih cepat. Dalam banyak kasus, perubahan kecil yang konsisten memberikan dampak jangka panjang lebih besar daripada perubahan besar yang tidak stabil.",
            f"Strategi yang bagus juga membuka ruang kolaborasi. Saat tim memahami tujuan yang sama, proses keputusan menjadi lebih cepat, lebih jelas, dan lebih toleran terhadap perbaikan. Dalam dunia yang bergerak cepat, kemampuan mengadaptasi strategi tanpa kehilangan fokus adalah karakteristik yang membedakan organisasi yang sehat dari yang hanya bereaksi terhadap pasang surut pasar.",
        ],
        "Tabel KPI, prioritas, dan checklist": [
            f"Untuk memastikan {label.lower()} benar-benar menghasilkan hasil, penting mempertahankan kerangka indikator. Tabel berikut membantu memvisualisasikan fokus utama yang biasa digunakan dalam evaluasi strategis.",
            "<table><thead><tr><th>Area</th><th>Indikator Utama</th><th>Tujuan Evaluasi</th></tr></thead><tbody><tr><td>Strategi</td><td>relevansi, tujuan, keselarasan</td><td>Menilai arah eksekusi</td></tr><tr><td>Operasional</td><td>kecepatan, konsistensi, pembagian tugas</td><td>Mengurangi hambatan eksekusi</td></tr><tr><td>Data</td><td>akurasi, validitas, jadwal update</td><td>Memastikan keputusan berbasis bukti</td></tr><tr><td>Pengalaman</td><td>engagement, feedback, kepuasan</td><td>Menjaga relevansi pembaca dan pengguna</td></tr></tbody></table>",
            "Checklist sederhana ini dapat dipakai sebagai acuan awal: definisikan tujuan utama, identifikasi audiens, buat metric yang dapat diukur, pilih alat yang sesuai, atur jadwal evaluasi, jalankan eksperimen kecil, dokumentasikan hasil, dan sesuaikan strategi berdasarkan data. Proses semacam ini sangat penting agar keputusan tetap masuk akal dan tidak berorientasi semata pada intuisi.",
            f"Pada praktiknya, indikator untuk {label.lower()} biasanya tidak sama antar industri. Tim marketing mungkin memusatkan perhatian pada konversi, content editor pada retention, sedangkan pelaku usaha mungkin fokus pada efisiensi biaya dan kualitas keputusan. Terlepas dari fokusnya, prinsipnya tetap sama: ukur apa yang penting, tetap konsisten, dan jadikan evaluasi sebagai bagian dari proses bukan sebagai kegiatan tambahan yang diabaikan.",
        ],
        "Risiko, hambatan, dan mitigasi": [
            f"Setiap strategi membawa risiko. Tanpa mitigasi yang tepat, {label.lower()} bisa berubah menjadi aktivitas yang menghabiskan sumber daya dengan hasil yang minim. Risiko yang umum terjadi adalah fokus pada volume di atas kualitas, interpretasi data yang terlalu simplistik, serta tekanan untuk cepat beraksi tanpa menyiapkan proses yang cukup.",
            f"Dalam konteks yang lebih luas, hambatan biasanya muncul ketika organisasi tidak memiliki pemahaman bersama tentang tujuan. Konsensus yang lemah akan menghasilkan keputusan yang boros, konflik internal, dan solusi yang tidak konsisten. Karena itu, penting untuk memiliki mekanisme review yang memungkinkan perbaikan terjadi secara terus-menerus tanpa menunggu masalah makin besar.",
            f"Mitigasi juga bisa dilakukan dengan membangun saluran feedback, menjaga dokumentasi proses, serta menyusun prioritas berdasarkan dampak dan urgensi. Strategi yang kuat bukan sekadar ideal, tetapi juga aman dari ambiguitas. Ketika pilihan dibuat dalam kerangka yang jelas, organisasi akan lebih siap menghadapi perubahan pasar dan tekanan operasional.",
            f"Kualitas pengambilan keputusan juga dipengaruhi oleh ketepatan interpretasi. Ketika pemimpin hanya melihat satu indikator atau satu sudut pandang, mereka dapat memutuskan hal yang sekilas tampak efektif tetapi tidak tahan lama. Oleh sebab itu, evaluasi yang komprehensif, perhatian pada konteks, dan keterbukaan terhadap masukan adalah langkah yang sangat penting.",
        ],
        "Implementasi praktis untuk tim dan individu": [
            f"Untuk tim dan individu, {label.lower()} harus dipahami sebagai aktivitas yang bisa ditangani dengan pendekatan terstruktur. Sebagai contoh, tim dapat mulai dengan sesi perencanaan 30 menit untuk menilai tujuan utama, batasan, dan indikator hasil. Setelah itu, mereka dapat menetapkan prioritas tiga hal yang paling berdampak, lalu mengevaluasi efektivitasnya dalam rentang waktu tertentu.",
            f"Pembaca juga dapat melakukan praktik sederhana dalam kehidupan profesional mereka. Bagi content strategist, itu berarti menguji tema sebelum menulis secara massal. Bagi pelaku bisnis, itu berarti menilai metrik kinerja sebelum mengalokasikan kapital tambahan. Bagi individu, itu berarti mengukur keputusan berdasarkan dampak jangka panjang bukan rekasi sesaat. Ketika prinsip ini dijalankan dengan konsisten, keputusan menjadi lebih matang dan bermanfaat.",
            f"Penerapan {label.lower()} bukan hanya tugas satu orang. Kolaborasi lintas fungsi, terutama antara tim operasional, pemasaran, analisis, dan eksekutif, sangat membantu karena masing-masing membawa perspektif berbeda. Dengan dialog yang produktif, organisasi dapat melihat celah yang mungkin tidak terlihat jika hanya berfokus pada satu unit kerja. Ini juga mengurangi kehilangan momentum akibat komunikasi yang terputus.",
            f"Hal yang penting adalah membentuk ritme kerja yang terukur: review, evaluasi, pembelajaran, dan iterasi. Ketika ritme ini berjalan secara rutin, organisasi dapat beradaptasi lebih cepat. Dengan begitu, {label.lower()} menjadi alat bukan hanya untuk analisis, tetapi juga untuk transformasi yang lebih stabil dan berkelanjutan.",
        ],
        "Pertanyaan umum dan jawaban cepat": [
            f"Apa yang menjadi pembeda antara strategi yang bagus dan strategi yang hanya menyerupai konsisten? Strategi yang bagus memiliki tujuan yang jelas, indikator yang terukur, alokasi sumber daya yang masuk akal, dan mekanisme perbaikan yang rutin. Strategi yang hanya tampak aktif biasanya tidak punya evaluasi yang baik dan cepat menghilang ketika hasilnya tidak sesuai harapan.",
            f"Apakah {label.lower()} harus diterapkan di semua line bisnis? Idealnya, ya, tetapi dengan penyesuaian. Setiap organisasi memiliki konteks, ukuran, dan tingkat kompleksitas yang berbeda. Yang paling penting adalah menyesuaikan model kerja agar sesuai kebutuhan, bukan memaksakan skema yang terlalu kompleks untuk kondisi yang sederhana.",
            f"Bagaimana cara mengukur hasil dalam jangka pendek dan panjang? Gunakan kombinasi indikator primer dan sekunder, termasuk kualitas keputusan, efektivitas eksekusi, serta dampak yang dirasakan pengguna atau audiens. Jangan hanya mengandalkan satu metrik karena satu angka tidak selalu mewakili realitas yang lebih luas.",
            f"Apakah {label.lower()} bisa dipelajari oleh pemula? Tentu, asalkan pendekatan yang digunakan sistematis dan realistis. Pemula bisa mulai dengan pemahaman dasar, observasi terhadap praktik yang relevan, lalu membangun pengalaman melalui eksperimen kecil. Kunci utamanya adalah konsistensi dan evaluasi, bukan kecepatan semata.",
        ],
        "Kesimpulan dan langkah berikutnya": [
            f"Secara keseluruhan, {label.lower()} memiliki peran penting dalam membentuk keputusan yang lebih sehat, relevan, dan cepat di era digital. Saat pasar berubah dengan cepat, organisasi yang mampu menghubungkan tujuan, data, eksekusi, dan evaluasi akan lebih siap menghadapi perubahan. Oleh karena itu, menilai {topic.lower()} tidak hanya dilakukan di level teknis, tetapi juga di level strategi dan budaya kerja.",
            f"Langkah berikutnya adalah mengubah pemahaman menjadi tindakan. Mulai dari satu area yang paling berpengaruh, tetapkan indikator yang jelas, dokumentasikan proses, dan lakukan review secara rutin. Itulah pendekatan yang lebih kuat dibanding mencoba menyelesaikan semuanya sekaligus dalam satu waktu.",
            f"Jika Anda ingin terus mengikuti perkembangan {label.lower()}, cermati topik terkait, evaluasi praktik yang sudah dijalankan, dan pelajari contoh nyata dari kasus yang relevan. Dengan kombinasi antara teori, konteks, dan eksekusi yang disiplin, Anda akan lebih siap menghadapi tantangan dan peluang di masa mendatang.",
            f"Semakin kuat kontrol Anda atas data, strategi, dan proses evaluasi, semakin besar peluang untuk menghasilkan keputusan yang berdampak. {label} bukan sekadar kata kunci; ia adalah alat berpikir yang dapat membantu individu dan organisasi membuat keputusan yang lebih matang, lebih relevan, dan lebih siap untuk masa depan.",
        ],
    }

    sections_html = []
    for index_section, title in enumerate(section_titles, 1):
        if title in paragraphs_by_section:
            sections_html.append(render_section(title, paragraphs_by_section[title]))

    internal_links = "\n".join(f'<li><a href="/category/{slug}/">{esc(link)}</a></li>' for slug, link in [
        (slugify(label), label),
        ("tech", "Tech"),
        ("health", "Health"),
        ("news", "News"),
        ("investasi", "Investasi"),
        ("bisnis", "Bisnis"),
        ("seo", "SEO"),
    ])
    external_links = "\n".join(f'<li><a href="{url}" target="_blank" rel="noopener noreferrer">{esc(name)}</a></li>' for name, url in EXTERNAL_LINKS.get(slugify(label), EXTERNAL_LINKS["default"]))
    related_block = "\n".join(f'<li><a href="{link}">{esc(text)}</a></li>' for text, link in [(text, text) for text in related_links[:7]])

    faq = """
    <div class="faq">
      <h3>FAQ</h3>
      <h4>Apakah artikel ini cocok untuk pemula?</h4>
      <p>Ya, artikel ini ditulis untuk membantu pemula memahami konsep dasar sebelum memasuki aspek yang lebih kompleks.</p>
      <h4>Bagaimana cara memulai penerapannya?</h4>
      <p>Mulai dari memahami tujuan, menentukan indikator, dan menerapkan eksperimen kecil sebelum memperluas skala.</p>
      <h4>Apakah sumber yang digunakan sudah terverifikasi?</h4>
      <p>Pastikan Anda memeriksa sumber, tanggal, dan konteks. Gunakan referensi primernya untuk keputusan yang lebih akurat.</p>
      <h4>Apakah konten ini bisa diubah?</h4>
      <p>Ya, silakan sesuaikan dengan kebutuhan redaksi, target audiens, dan kebijakan editorial masing-masing platform.</p>
    </div>
    """

    conclusion = """
    <section>
      <h2>Kesimpulan</h2>
      <p>{label} bukan hanya topik yang populer, tetapi juga fondasi untuk keputusan yang lebih sehat dan lebih relevan dalam lingkungan digital yang cepat berubah. Keberhasilan muncul ketika strategi, eksekusi, dan evaluasi saling menyokong. Oleh karena itu, prioritaskan pemahaman yang benar, praktik yang konsisten, dan pembelajaran yang berulang.</p>
      <p>Langkah selanjutnya adalah menerapkan satu strategi yang paling berdampak pada konteks Anda, lalu evaluasi hasilnya dalam jangka pendek dan jangka panjang. Dengan cara ini, Anda akan memiliki fondasi yang lebih kuat untuk terus berkembang dan menjadikan {label.lower()} sebagai alat keputusan yang bermanfaat.</p>
    </section>
    """

    return f"""
    <div class="toc">
      <h2>Daftar Isi</h2>
      <ol>
        <li><a href="#bagian-1">Pengantar dan urgensi topik</a></li>
        <li><a href="#bagian-2">Dasar pemahaman dan definisi</a></li>
        <li><a href="#bagian-3">Konteks pasar dan tren Indonesia</a></li>
        <li><a href="#bagian-4">Strategi eksekusi yang tepat</a></li>
        <li><a href="#bagian-5">Tabel KPI, prioritas, dan checklist</a></li>
        <li><a href="#bagian-6">Risiko, hambatan, dan mitigasi</a></li>
        <li><a href="#bagian-7">Implementasi praktis untuk tim dan individu</a></li>
        <li><a href="#bagian-8">Pertanyaan umum dan jawaban cepat</a></li>
        <li><a href="#bagian-9">Kesimpulan dan langkah berikutnya</a></li>
      </ol>
    </div>
    <div class="share-links">
      <h3>Bagikan Artikel</h3>
      <p><a href="https://www.facebook.com/sharer/sharer.php?u={quote(SITE_URL, safe=':/')}" target="_blank" rel="noopener noreferrer">Facebook</a> | 
      <a href="https://www.linkedin.com/sharing/share-offsite/?url={quote(SITE_URL, safe=':/')}" target="_blank" rel="noopener noreferrer">LinkedIn</a> |
      <a href="https://wa.me/?text={quote(f'{topic} {label} — ' + SITE_URL)}" target="_blank" rel="noopener noreferrer">WhatsApp</a></p>
    </div>
    {sections_html[0]} 
    {sections_html[1]} 
    {sections_html[2]} 
    {sections_html[3]} 
    {sections_html[4]} 
    {sections_html[5]} 
    {sections_html[6]} 
    {sections_html[7]} 
    {sections_html[8]} 
    {conclusion}
    <section>
      <h2>7 Internal Link yang Relevan</h2>
      <ul>{internal_links}</ul>
    </section>
    <section>
      <h2>7 External Link yang Sesuai</h2>
      <ul>{external_links}</ul>
    </section>
    <section>
      <h2>Konten Terkait</h2>
      <ul>{related_block}</ul>
    </section>
    {faq}
    """


def make_jsonld(title: str, description: str, category: str, url: str, article_date: str, faq_items: list[dict]) -> dict:
    faq_array = []
    for item in faq_items:
        faq_array.append({
            "@type": "Question",
            "name": item.get("question", ""),
            "acceptedAnswer": {
                "@type": "Answer",
                "text": item.get("answer", "")
            }
        })
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": title,
                "description": description,
                "datePublished": article_date,
                "dateModified": article_date,
                "author": {"@type": "Organization", "name": SITE_NAME},
                "publisher": {"@type": "Organization", "name": SITE_NAME},
                "mainEntityOfPage": SITE_URL + url,
                "articleSection": category,
                "inLanguage": "id-ID",
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_array,
            },
        ],
    }


def page_shell(title: str, description: str, canonical_path: str, body_html: str, *, jsonld: dict | None = None, noindex: bool = False) -> str:
    canonical_url = SITE_URL + canonical_path
    robots = "noindex,follow" if noindex else "index,follow,max-image-preview:large"
    json_ld = json.dumps(jsonld or {}, ensure_ascii=False)
    nav_links = [
        ("/", "Beranda"),
        ("/category/investasi/", "Investasi"),
        ("/category/tech/", "Tech"),
        ("/category/health/", "Health"),
        ("/category/news/", "News"),
        ("/contact-us.html", "Kontak"),
    ]
    nav = "".join(f'<a href="{href}">{esc(text)}</a>' for href, text in nav_links)
    footer = "".join(f'<a href="/{slug}.html">{esc(label)}</a>' for slug, (_, label) in LEGAL_PAGES.items())
    return f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{esc(title)} | {SITE_NAME}</title>
  <meta name="description" content="{esc(description)}" />
  <meta name="robots" content="{robots}" />
  <meta name="author" content="{SITE_NAME}" />
  <meta name="google-adsense-account" content="{ADSENSE_CLIENT}" />
  <link rel="canonical" href="{esc(canonical_url)}" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{esc(canonical_url)}" />
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(description)}" />
  <meta property="og:image" content="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200&auto=format&fit=crop&q=80" />
  <meta property="og:site_name" content="{SITE_NAME}" />
  <meta property="og:locale" content="id_ID" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{esc(title)}" />
  <meta name="twitter:description" content="{esc(description)}" />
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>
  <script type="application/ld+json">{json_ld}</script>
  <style>
    :root {{
      --bg: #f3f6fb; --panel: #fff; --text: #1f2a37; --muted: #5b677a; --brand: #1148c9; --line: #dde6f2; --accent: #edf3ff;
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; font-family: Arial, sans-serif; background: var(--bg); color: var(--text); line-height: 1.8; }}
    a {{ color: var(--brand); text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}
    header, footer {{ background: #fff; border-bottom: 1px solid var(--line); }}
    header {{ position: sticky; top: 0; z-index: 20; }}
    nav {{ max-width: 1180px; margin: 0 auto; padding: 16px 20px; display: flex; flex-wrap: wrap; gap: 16px; align-items: center; }}
    main {{ max-width: 1180px; margin: 0 auto; padding: 24px 20px 60px; }}
    article, .card {{ background: var(--panel); border: 1px solid var(--line); border-radius: 16px; padding: 24px; box-shadow: 0 8px 30px rgba(17,72,201,0.03); margin-bottom: 26px; }}
    h1, h2, h3, h4, h5, h6 {{ line-height: 1.3; margin-top: 1.4em; }}
    h1 {{ font-size: clamp(2rem, 3vw, 3rem); }}
    h2 {{ font-size: clamp(1.5rem, 2vw, 2.1rem); }}
    h3 {{ font-size: 1.15rem; }}
    p {{ margin: 0 0 1.2em; }}
    ul, ol {{ padding-left: 1.2em; }}
    .muted {{ color: var(--muted); }}
    .toc {{ background: var(--accent); border: 1px solid var(--line); border-radius: 12px; padding: 20px; margin-bottom: 24px; }}
    .faq {{ background: #f8fafc; border: 1px solid var(--line); border-radius: 12px; padding: 20px; }}
    table {{ width: 100%; border-collapse: collapse; margin: 1.5em 0; }}
    th, td {{ border: 1px solid var(--line); padding: 12px; text-align: left; }}
    th {{ background: #f5f8ff; }}
    .ads-slot {{ background: #eceff5; border: 1px dashed #c0c9d8; text-align: center; padding: 12px; border-radius: 8px; color: var(--muted); margin: 20px 0; }}
    footer nav {{ padding: 18px 20px 24px; display: flex; flex-wrap: wrap; gap: 16px; }}
    .footer-note {{ max-width: 1180px; margin: 0 auto; padding: 0 20px 30px; color: var(--muted); }}
    @media (max-width: 700px) {{ nav {{ gap: 10px; }} article, .card {{ padding: 18px; }} }}
  </style>
</head>
<body>
  <header>
    <nav aria-label="Main navigation">
      <a href="/" style="font-weight:bold; color:var(--text);">{SITE_NAME}</a>
      {nav}
    </nav>
  </header>
  <main>
    <article>
      {body_html}
    </article>
  </main>
  <footer>
    <nav aria-label="Footer navigation">
      {footer}
      <a href="/sitemap.xml">Sitemap</a>
      <a href="/regions/">Regional</a>
    </nav>
    <div class="footer-note">© {date.today().year} {SITE_NAME}. Semua konten perlu diverifikasi redaksi sebelum dipublish sepenuhnya.</div>
  </footer>
</body>
</html>
'''


def write_page(root: Path, relative_path: str, content: str) -> None:
    path = root / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def generate_articles(output_dir: Path, articles_per_category: int, min_words: int) -> list[dict]:
    generated = []
    article_counter = 1
    for category_name, label in CATEGORIES.items():
        for idx in range(1, articles_per_category + 1):
            article = make_article_intro(label, idx, label, str(date.today().year), str(date.today().month).zfill(2))
            article["slug"] = f"{slugify(label)}-{idx}"
            article["category_slug"] = category_name
            article["path"] = article_path(category_name, article["slug"], article["year"], article["month"])
            article["internal_links"] = [
                ("Investasi", "/category/investasi/"),
                ("Tech", "/category/tech/"),
                ("Health", "/category/health/"),
                ("News", "/category/news/"),
                ("Bisnis", "/category/bisnis/"),
                ("SEO", "/category/seo/"),
                ("Kontak", "/contact-us.html"),
            ]
            article["faq"] = [
                {"question": f"Apa inti dari {label.lower()}?", "answer": f"Inti dari {label.lower()} adalah menjelaskan maksud, konteks, dan cara eksekusi yang bisa diukur dengan jelas."},
                {"question": "Bagaimana cara menerapkan strategi ini secara bertahap?", "answer": "Mulai dari analisis tujuan, pilih indikator utama, evaluasi hasil, lalu perbaiki proses secara berkala."},
                {"question": "Apakah artikel ini bisa dimodifikasi untuk kebutuhan redaksi?", "answer": "Ya, artikel ini dibuat sebagai template dasar yang bisa disesuaikan dengan target pembaca, bahasa, dan kebijakan editorial."},
            ]
            article["article_html"] = build_article_body(label, label, idx, [
                f"{label} untuk pembaca Indonesia",
                f"Strategi {label.lower()} yang relevan",
                f"Checklist {label.lower()} mingguan",
                f"KPI dan evaluasi {label.lower()}",
                f"Panduan {label.lower()} lanjutan",
                f"Contoh strategi {label.lower()} yang praktis",
                f"Riset {label.lower()} terbaru",
            ], article["internal_links"])
            faq_count = word_count(article["article_html"])
            article["word_count"] = faq_count
            generated.append(article)
    return generated


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", re.sub(r"<[^>]+>", " ", text), flags=re.UNICODE))


def build_homepage(articles: list[dict]) -> str:
    posts = "".join(f'<li><a href="/{esc(a["path"]) }">{esc(a["title"])}</a> <span class="muted">{esc(a["category"])}</span></li>' for a in sorted(articles, key=lambda x: x["date"], reverse=True)[:6])
    popular = "".join(f'<li><a href="/{esc(a["path"]) }">{esc(a["title"])}</a></li>' for a in sorted(articles, key=lambda x: x["word_count"], reverse=True)[:5])
    cards = "".join(f'<li><a href="/category/{slug}/">{esc(name)}</a></li>' for slug, name in CATEGORIES.items())
    return f'''<h1>{SITE_NAME}</h1>
<p>Portal edukasi, bisnis, teknologi, kesehatan, dan investasi berbasis SEO untuk pembaca Indonesia. Semua konten dibuat untuk kebutuhan online editorial dan siap diperbarui sesuai kebutuhan redaksi.</p>
<div class="toc"><h2>Postingan Terkini</h2><ul>{posts}</ul></div>
<div class="toc"><h2>Postingan Populer</h2><ul>{popular}</ul></div>
<div class="toc"><h2>Kategori</h2><ul>{cards}</ul></div>
<div class="toc"><h2>Regional</h2><ul>{''.join(f'<li><a href="/regions/{slugify(region)}.html">{esc(region)}</a></li>' for region in REGIONS)}</ul></div>
'''


def build_category_page(category_slug: str, category_name: str, articles: list[dict]) -> str:
    items = "".join(f'<li><a href="/{esc(a["path"]) }">{esc(a["title"])}</a> · {esc(a["date"])}</li>' for a in articles if a["category_slug"] == category_slug)
    return f'''<h1>{esc(category_name)}</h1><p>Artikel {esc(category_name)} yang dibuat secara otomatis untuk mendukung struktur SEO dan navigasi situs.</p><ul>{items}</ul>'''


def build_legal_page(title: str, description: str, slug: str) -> str:
    return f'''<h1>{esc(title)}</h1><p>{esc(description)}</p>'''


def build_region_page(region: str) -> str:
    return f'''<h1>Informasi Regional {esc(region)}</h1><p>Halaman regional {esc(region)} dibuat untuk mendukung struktur situs, navigasi wilayah, dan keperluan SEO lokal. Pastikan content lokal diverifikasi dan diperbarui bila ada perubahan data atau kebijakan.</p>
<p><a href="/contact-us.html">Hubungi redaksi</a> untuk koreksi, validasi, atau kebutuhan editorial.</p>'''


def build_sitemap(articles: list[dict]) -> str:
    urls = ["/", "/contact-us.html", "/about-us.html", "/sitemap.html", "/disclaimer.html", "/privacy-policy.html", "/terms.html", "/license.html", "/join-forum.html", "/pedoman-siber.html", "/cookies.html", "/regions/", *[f"/{a['path']}" for a in articles]]
    for region in REGIONS:
        urls.append(f"/regions/{slugify(region)}.html")
    for slug, _ in CATEGORIES.items():
        urls.append(f"/category/{slug}/")
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    for url in sorted(set(urls)):
        xml += f"<url><loc>{esc(SITE_URL + url)}</loc></url>"
    xml += "</urlset>"
    return xml


def generate_site(output_dir: Path, articles_per_category: int = DEFAULT_ARTICLES_PER_CATEGORY, min_words: int = MIN_WORDS) -> None:
    articles = generate_articles(output_dir, articles_per_category, min_words)

    # Homepage
    write_page(output_dir, "index.html", page_shell(SITE_NAME, "Portal berita, investasi, teknologi, kesehatan, bisnis, dan SEO berbasis Indonesia.", "/", build_homepage(articles), jsonld={"@context": "https://schema.org", "@type": "WebSite", "name": SITE_NAME, "url": SITE_URL + "/"}))

    # Category pages
    for category_slug, category_name in CATEGORIES.items():
        matching = [a for a in articles if a["category_slug"] == category_slug]
        write_page(output_dir, f"category/{category_slug}/index.html", page_shell(f"{category_name} | {SITE_NAME}", f"Kumpulan artikel {category_name.lower()} terbaru dan paling relevan untuk kebutuhan editorial dan SEO.", f"/category/{category_slug}/", build_category_page(category_slug, category_name, matching)))

    # Region pages
    write_page(output_dir, "regions/index.html", page_shell("Regional Indonesia", "Indeks regional Indonesia.", "/regions/", "<h1>Regional Indonesia</h1>" + "".join(f'<li><a href="/regions/{slugify(region)}.html">{esc(region)}</a></li>' for region in REGIONS)))
    for region in REGIONS:
        write_page(output_dir, f"regions/{slugify(region)}.html", page_shell(f"{region} | {SITE_NAME}", f"Halaman regional {region}.", f"/regions/{slugify(region)}.html", build_region_page(region)))

    # Legal pages
    legal_copy = {
        "about-us": "Geturnet Ltd adalah jaringan editorial dan usaha digital yang fokus pada konten edukasi, analisis bisnis, teknologi, kesehatan, dan investasi. Kami membangun platform informasi yang membantu pembaca mengambil keputusan lebih baik berdasarkan data, sumber yang relevan, dan konteks yang jelas.",
        "contact-us": "Hubungi tim redaksi melalui form atau saluran email yang sudah Anda atur di repositori. Untuk situs statis GitHub Pages, validasi kontak perlu disertai kanal email atau layanan pihak ketiga yang aman.",
        "sitemap": "Sitemap memuat indeks halaman utama, kategori, artikel, legal pages, dan halaman regional untuk memudahkan navigasi robot mesin pencari dan pengunjung.",
        "disclaimer": "Semua konten yang tersedia di situs ini ditujukan untuk tujuan edukasi umum. Pembaca disarankan untuk melakukan verifikasi lanjutan sebelum mengambil keputusan penting, terutama yang berkaitan dengan kesehatan, investasi, hukum, dan bisnis.",
        "privacy-policy": "Kebijakan privasi situs perlu diperbarui sesuai praktik pengumpulan data yang benar-benar aktif. Jelaskan jenis data yang dikumpulkan, tujuan penggunaan, retensi, vendor pihak ketiga, serta mekanisme opt-out bila ada.",
        "terms": "Syarat penggunaan situs meliputi hak pemanfaatan, keterbatasan tanggung jawab, dan kewajiban pengguna dalam memanfaatkan konten secara aseptik dan sesuai hukum yang berlaku.",
        "license": "Semua konten, kode, dan aset yang dikembangkan di repositori ini perlu memiliki lisensi yang jelas sesuai sumberdaya yang digunakan. Periksa semua aset pihak ketiga sebelum publikasi massal.",
        "join-forum": "Forum komunitas dapat dikembangkan untuk membangun diskusi yang sehat mengenai investasi, teknologi, kesehatan, dan topik strategis lainnya. Pastikan aturan moderasi, keamanan, dan kode etik komunitas dikonfirmasi sebelum dibuka untuk umum.",
        "pedoman-siber": "Perhatikan keamanan akun pengguna, perlindungan data, penggunaan kata sandi kuat, dan pencegahan serangan siber sebelum situs dipublikasikan secara luas.",
        "cookies": "Pengelolaan cookies dan teknologi pengingat perlu dijelaskan secara jelas untuk menyesuaikan dengan kebijakan hukum, analitik, dan kebutuhan iklan yang dipakai.",
    }
    for slug, (page_title, nav_label) in LEGAL_PAGES.items():
        write_page(output_dir, f"{slug}.html", page_shell(page_title, legal_copy[slug], f"/{slug}.html", build_legal_page(page_title, legal_copy[slug], slug)))

    # Article pages
    for article in articles:
        faq = article["faq"]
        article_url = f"/{article['path']}"
        article_body = article["article_html"]
        article_jsonld = make_jsonld(article["title"], article["description"], article["category"], article_url, article["date"], faq)
        if min_words and word_count(article_body) < min_words:
            noindex = True
            label_status = "DRAFT / noindex"
        else:
            noindex = False
            label_status = "Siap dipublish"
        article_shell = page_shell(article["title"], article["description"], article_url, f"<h1>{esc(article['title'])}</h1><p class=\"muted\">{esc(article['category'])} · {esc(article['date'])} · {label_status}</p>{article_body}", jsonld=article_jsonld, noindex=noindex)
        write_page(output_dir, article["path"], article_shell)

    # Sitemap
    write_page(output_dir, "sitemap.xml", build_sitemap(articles))

    print(f"Generated {len(articles)} articles into {output_dir.resolve()}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate static Geturnet SEO pages.")
    parser.add_argument("--output", type=Path, default=Path("."), help="Directory output")
    parser.add_argument("--articles-per-category", type=int, default=DEFAULT_ARTICLES_PER_CATEGORY, help="Articles generated per category")
    parser.add_argument("--min-words", type=int, default=MIN_WORDS, help="Minimum word count before article is eligible for index")
    args = parser.parse_args()
    generate_site(args.output, args.articles_per_category, args.min_words)


if __name__ == "__main__":
    main()
