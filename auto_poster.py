import os
import datetime
from bs4 import BeautifulSoup

# Konfigurasi Direktori Blog
HTML_FILE = "index.html"

def generate_article_html(title, category, summary, image_url):
    """Template komponen berita baru untuk disisipkan ke halaman web"""
    timestamp = datetime.datetime.now().strftime("%d %B %Y, %H:%M WIB")
    html_snippet = f"""
    <div class="news-card">
        <img src="{image_url}" alt="{title}">
        <span class="category-tag">{category}</span>
        <h3>{title}</h3>
        <div class="meta-info">{timestamp} • {summary[:60]}...</div>
    </div>
    """
    return html_snippet

def update_website(new_title, category, summary, image_url):
    if not os.path.exists(HTML_FILE):
        print(f"File {HTML_FILE} tidak ditemukan!")
        return

    with open(HTML_FILE, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Cari grid berita terbaru untuk menyisipkan artikel baru
    news_grid = soup.find("div", class_="news-grid")
    if news_grid:
        new_card_soup = BeautifulSoup(generate_article_html(new_title, category, summary, image_url), "html.parser")
        news_grid.insert(0, new_card_soup)

        # Simpan kembali file HTML
        with open(HTML_FILE, "w", encoding="utf-8") as file:
            file.write(str(soup))
        print(f"Sukses! Artikel baru '{new_title}' berhasil dipublish ke {HTML_FILE}")
    else:
        print("Elemen .news-grid tidak ditemukan pada struktur HTML.")

if __name__ == "__main__":
    print("--- Generator Artikel Otomatis Geturnet ---")
    
    # Contoh data berita otomatis yang bisa dihubungkan ke AI / RSS Feeds
    sample_title = "Inovasi Terbaru Teknologi Cloud dan AI Mengubah Lanskap Bisnis Global"
    sample_category = "Tech"
    sample_summary = "Perusahaan teknologi global berlomba mengintegrasikan machine learning untuk efisiensi operasional..."
    sample_image = "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=500&q=80"

    update_website(sample_title, sample_category, sample_summary, sample_image)
