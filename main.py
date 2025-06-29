from flask import Flask, request, render_template
from urllib import request as urlrequest
from bs4 import BeautifulSoup
import urllib.error

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_url = request.form.get('url')

        try:
            # 1. URL 열기
            response = urlrequest.urlopen(input_url, timeout=5)
            html = response.read()

            # 2. BeautifulSoup 파싱
            soup = BeautifulSoup(html, 'html.parser')

            # 3. 기본 분석
            titles = soup.find_all(['h1', 'h2', 'h3'])
            images = soup.find_all('img')
            links = soup.find_all('a')

            analysis = {
                '입력한 URL': input_url,
                '제목 개수': len(titles),
                '이미지 개수': len(images),
                '링크 개수': len(links),
                '링크 목록': [a.get('href') for a in links if a.get('href')]
            }

            return render_template("result.html", analysis=analysis)

        except urllib.error.URLError:
            return render_template("form.html", error="유효하지 않은 URL입니다.")
        except Exception as e:
            return render_template("form.html", error=f"예외 발생: {e}")

    return render_template("form.html")


if __name__ == '__main__':
    app.run(debug=True)