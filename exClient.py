import requests
import base64

# 서버 주소
SERVER_URL = "http://localhost:5000"


# 01. 텍스트 전송 (JSON)
def send_text():
    payload = {"message": "안녕하세요, Flask!"}
    res = requests.post(f"{SERVER_URL}/text", json=payload)
    print("텍스트 응답:", res.json())


# 02. 이미지 파일 전송 (multipart/form-data)
def send_image_file():
    with open("example.jpg", "rb") as img_file:
        files = {"image": img_file}
        res = requests.post(f"{SERVER_URL}/upload-image", files=files)
        print("파일 업로드 응답:", res.json())


# 03. Base64 이미지 전송 (JSON)
def send_image_base64():
    with open("example.jpg", "rb") as img_file:
        b64_encoded = base64.b64encode(img_file.read()).decode('utf-8')
        payload = {
            "image": f"data:image/jpeg;base64,{b64_encoded}"
        }
        res = requests.post(f"{SERVER_URL}/upload-base64", json=payload)
        print("Base64 업로드 응답:", res.json())


# 실행 예시
send_text()
send_image_file()
send_image_base64()