import requests
import re
from bs4 import BeautifulSoup

BASE_URL = "https://hoadaotv.info"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Referer": BASE_URL
}

def get_match_data():
    matches = []
    try:
        # 1. Lấy trang chủ
        res_home = requests.get(BASE_URL, headers=HEADERS, timeout=15)
        soup_home = BeautifulSoup(res_home.text, 'html.parser')
        
        # Tìm tất cả link có chữ /truc-tiep/
        links = []
        for a in soup_home.find_all('a', href=True):
            href = a['href']
            if '/truc-tiep/' in href:
                url = href if href.startswith('http') else BASE_URL + href
                if url not in links:
                    links.append(url)
        
        print(f"Tìm thấy {len(links)} link trận đấu.")

        for url in links:
            try:
                res_detail = requests.get(url, headers=HEADERS, timeout=10)
                html = res_detail.text
                
                # Tìm link FLV bằng Regex (chính xác nhất)
                flv_match = re.search(r'"flv":"([^"]+)"', html)
                if not flv_match:
                    continue
                
                stream_url = flv_match.group(1).replace('\\/', '/')
                
                # Tìm tên trận đấu (Thử nhiều thẻ khác nhau)
                soup_detail = BeautifulSoup(html, 'html.parser')
                title = "Trận đấu không tên"
                h1 = soup_detail.find('h1')
                if h1:
                    title = h1.get_text(strip=True)
                
                # Tìm Logo (Lấy cái ảnh đầu tiên trong khung live)
                logo = "https://hoadaotv.info/favicon.ico"
                img = soup_detail.find('img', src=re.compile(r'\.(png|jpg|jpeg|webp)'))
                if img:
                    logo = img['src'] if img['src'].startswith('http') else BASE_URL + img['src']

                matches.append({
                    "name": title,
                    "logo": logo,
                    "url": stream_url
                })
                print(f"Đã lấy thành công: {title}")
            except Exception as e:
                print(f"Lỗi khi quét link {url}: {e}")
                
        return matches
    except Exception as e:
        print(f"Lỗi trang chủ: {e}")
        return []

def write_m3u(matches):
    # Nếu không có trận nào, không ghi đè để giữ lại file cũ (hoặc ghi file trống tùy bạn)
    if not matches:
        print("Không tìm thấy trận nào đang live!")
        return

    content = "#EXTM3U\n"
    for m in matches:
        content += f'#EXTINF:-1 tvg-logo="{m["logo"]}" group-title="Hoa Dao TV", {m["name"]}\n'
        content += f'#EXTVLCOPT:http-referrer={BASE_URL}/\n'
        content += f'#EXTVLCOPT:http-user-agent=Mozilla/5.0\n'
        content += f'{m["url"]}\n\n'
    
    with open('watchfrhd.m3u', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    data = get_match_data()
    write_m3u(data)
