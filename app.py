from flask import Flask, render_template, request
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form.get('message')

    # 生成 RSA 密鑰對
    key = RSA.generate(2048)
    public_key = key.publickey()

    # 使用公鑰對消息進行加密
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message.encode())

    return render_template('result.html', message=message, public_key=public_key.export_key().decode(), encrypted_message=encrypted_message.hex())

if __name__ == '__main__':
    app.run(debug=True)
