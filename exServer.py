from flask import Flask, request, jsonify
import base64
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# 01. 텍스트 전송 (JSON)
@app.route('/text', methods=['POST'])
def receive_text():
    data = request.get_json()
    message = data.get("message")
    return jsonify({"received": message})


# 02. 이미지 파일 전송 (multipart/form-data)
@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400

    image = request.files['image']
    filename = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(filename)
    return jsonify({"status": "image uploaded", "filename": image.filename})


# 03. 이미지 Base64 전송 (JSON)
@app.route('/upload-base64', methods=['POST'])
def upload_base64():
    data = request.get_json()
    b64_data = data.get('image')

    # Remove data URI prefix if present
    if b64_data.startswith("data:image"):
        b64_data = b64_data.split(",")[1]

    image_bytes = base64.b64decode(b64_data)
    with open(os.path.join(UPLOAD_FOLDER, 'decoded_image.png'), 'wb') as f:
        f.write(image_bytes)

    return jsonify({"status": "base64 image saved"})


if __name__ == '__main__':
    app.run(debug=True)