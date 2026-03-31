import requests
import re
from bs4 import BeautifulSoup

# Cấu hình nguồn
BASE_URL = "https://hoadaotv.info"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": BASE_URL
}

def get_match_data():
    try:
        # 1. Lấy danh sách trận đấu ở trang chủ
        response = requests.get(BASE_URL, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        matches = []
        # Tìm các link trận đấu (thường nằm trong các thẻ a có chứa /truc-tiep/)
        links = set()
        for a in soup.find_all('a', href=True):
            if '/truc-tiep/' in a['href']:
                full_url = a['href'] if a['href'].startswith('http') else BASE_URL + a['href']
                links.add(full_url)

        for url in links:
            try:
                res = requests.get(url, headers=HEADERS, timeout=10)
                html = res.text
                s = BeautifulSoup(html, 'html.parser')

                # Lấy tên trận và BLV
                title = s.find('h1').text.strip() if s.find('h1') else "Trận đấu"
                # Tìm logo (thường là cái đầu tiên trong khung trận đấu)
                logo_img = s.find('img', {'class': 'logo'}) or s.find('img', src=re.compile(r'logo'))
                logo_url = logo_img['src'] if logo_img else "https://hoadaotv.info/favicon.ico"

                # Dùng Regex móc link stream trong biến serverStreamLinks
                flv_match = re.search(r'"flv":"([^"]+)"', html)
                
                if flv_match:
                    matches.append({
                        "name": title,
                        "logo": logo_url,
                        "url": flv_match.group(1).replace('\\/', '/')
                    })
            except:
                continue
        return matches
    except:
        return []

def write_m3u(matches):
    content = "#EXTM3U\n"
    for m in matches:
        # Định dạng M3U nâng cao có Logo
        content += f'#EXTINF:-1 tvg-logo="{m["logo"]}" group-title="Hoa Dao TV", {m["name"]}\n'
        # Header để VLC không bị server chặn
        content += f'#EXTVLCOPT:http-referrer={BASE_URL}/\n'
        content += f'#EXTVLCOPT:http-user-agent=Mozilla/5.0\n'
        content += f'{m["url"]}\n\n'
    
    with open('watchfrhd.m3u', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    data = get_match_data()
    if data:
        write_m3u(data)
        print(f"Thành công! Đã lấy được {len(data)} trận.")
