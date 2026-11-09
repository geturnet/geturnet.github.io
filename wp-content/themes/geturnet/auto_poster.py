import os
import datetime
from bs4 import BeautifulSoup

HTML_FILE = "index.html"

# Kode Unit Iklan Google AdSense Anda
ADSENSE_AD_CODE = """
<div class="adsense-box" style="margin: 20px 0; text-align: center;">
    <ins class="adsbygoogle"
         style="display:block"
         data-ad-client="ca-pub-4549220738609468"
         data-ad-slot="1234567890"
         data-ad-format="auto"
         data-full-width-responsive="true"></ins>
    <script>
         (adsbygoogle = window.adsbygoogle || []).push({});
    </script>
</div>
"""

def generate_article_html(title, category, summary, image_url):
    timestamp = datetime.datetime.now().strftime("%d %B %Y, %H:%M WIB")
    html_snippet = f"""
    <div class="news-card">
        <img src="{image_url}" alt="{title}">
        <span class="category-tag">{category}</span>
        <h3>{title}</h3>
        <div class="meta-info"><i class="far fa-clock"></i> {timestamp}</div>
        {ADSENSE_AD_CODE}
    </div>
    """
    return html_snippet

def update_website():
    if not os.path.exists(HTML_FILE):
        print(f"File {HTML_FILE} tidak ditemukan!")
        return

    with open(HTML_FILE, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    news_grid = soup.find("div", class_="news-grid")
    if news_grid:
        current_date = datetime.datetime.now().strftime("%d %b %Y")
        new_title = f"Perkembangan Terbaru Teknologi AI dan Riset Digital Terkini: {current_date}"
        category = "Tech"
        summary = "Integrasi kecerdasan buatan semakin mendominasi berbagai sektor industri di tanah air."
        image_url = "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=500&q=80"

        new_card_soup = BeautifulSoup(generate_article_html(new_title, category, summary, image_url), "html.parser")
        news_grid.insert(0, new_card_soup)

        with open(HTML_FILE, "w", encoding="utf-8") as file:
            file.write(str(soup))
        print("Sukses! Artikel baru dan unit iklan AdSense berhasil disisipkan.")
    else:
        print("Elemen .news-grid tidak ditemukan pada struktur HTML.")

if __name__ == "__main__":
    update_website()
