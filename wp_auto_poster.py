import base64
import requests
import datetime

# Konfigurasi WordPress Anda
WP_SITE = "https://geturnet.github.io" # Ganti dengan URL WordPress Anda (misal: https://geturnet.com)
WP_USER = "username_admin_wp"
WP_APP_PASSWORD = "xxxx xxxx xxxx xxxx" # Application password dari WP

def post_to_wordpress(title, content, category_name, image_url):
    api_url = f"{WP_SITE}/wp-json/wp/v2/posts"
    
    # Autentikasi Basic menggunakan Application Passwords
    credentials = f"{WP_USER}:{WP_APP_PASSWORD}"
    token = base64.b64encode(credentials.encode()).decode()
    
    headers = {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json"
    }
    
    # Data Artikel
    post_data = {
        "title": title,
        "content": content,
        "status": "publish", # Langsung publish atau ubah ke "draft"
        "excerpt": content[:150] + "..."
    }
    
    response = requests.post(api_url, json=post_data, headers=headers)
    
    if response.status_code == 201:
        print(f"Sukses mempublish artikel ke WordPress: {title}")
    else:
        print(f"Gagal mempublish: {response.json()}")

if __name__ == "__main__":
    current_time = datetime.datetime.now().strftime("%d %B %Y")
    
    sample_title = f"Riset & Perkembangan AI Terbaru di Indonesia: {current_time}"
    sample_content = "<p>Integrasi kecerdasan buatan dan generative engine optimization kini menjadi fokus utama perusahaan teknologi nasional dalam memperluas jangkauan informasi digital.</p>"
    
    post_to_wordpress(sample_title, sample_content, "Tech", "")
