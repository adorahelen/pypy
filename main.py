from flask import Flask, request, render_template
from urllib import request as urlrequest
from urllib.parse import urljoin
from bs4 import BeautifulSoup, Comment
import urllib.error

app = Flask(__name__)

def try_fetch_text(url):
    try:
        response = urlrequest.urlopen(url, timeout=5)
        return response.read().decode('utf-8', errors='ignore')
    except:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_url = request.form.get('url')

        try:
            response = urlrequest.urlopen(input_url, timeout=5)
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')

            # 제목, 이미지, 링크 추출
            titles = soup.find_all(['h1', 'h2', 'h3'])
            all_images = soup.find_all('img')
            links = soup.find_all('a')

            # 이미지 필터링
            supported_formats = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg')
            filtered_images = []
            for img in all_images:
                src = img.get('src')
                if src:
                    abs_url = urljoin(input_url, src)
                    if any(abs_url.lower().endswith(ext) for ext in supported_formats):
                        filtered_images.append(abs_url)

            # CSS/JS 파일 수집
            css_files = [
                urljoin(input_url, link.get('href'))
                for link in soup.find_all('link', rel='stylesheet')
                if link.get('href')
            ]
            js_files = [
                urljoin(input_url, script.get('src'))
                for script in soup.find_all('script') if script.get('src')
            ]

            # robots.txt / sitemap.xml 수집
            robots_txt = try_fetch_text(urljoin(input_url, '/robots.txt'))
            sitemap_xml = try_fetch_text(urljoin(input_url, '/sitemap.xml'))

            # JS 코드 내 위험 함수 스캔
            dangerous_keywords = ['eval', 'document.write', 'innerHTML', 'localStorage', 'token', 'auth', 'key']
            js_analysis_results = []
            for js_url in js_files[:5]:  # 최대 5개까지 분석
                js_code = try_fetch_text(js_url)
                if js_code:
                    findings = [kw for kw in dangerous_keywords if kw in js_code]
                    if findings:
                        js_analysis_results.append({
                            'url': js_url,
                            'keywords': findings
                        })

            analysis = {
                '입력한 URL': input_url,
                '제목 개수': len(titles),
                '이미지 개수': len(filtered_images),
                '링크 개수': len(links),
                '링크 목록': [urljoin(input_url, a.get('href')) for a in links if a.get('href')],
                '이미지 목록': filtered_images,
                'CSS 파일 목록': css_files,
                'JS 파일 목록': js_files,
                'robots.txt': robots_txt if robots_txt else '없음',
                'sitemap.xml': sitemap_xml if sitemap_xml else '없음',
                '위험한 JS 분석 결과': js_analysis_results
            }

            return render_template("result.html", analysis=analysis)

        except urllib.error.URLError:
            return render_template("form.html", error="유효하지 않은 URL입니다.")
        except Exception as e:
            return render_template("form.html", error=f"예외 발생: {e}")

    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)