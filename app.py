from flask import Flask, render_template, request
import hashlib
import ecdsa

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    message = request.form.get('message')
    private_key = ecdsa.SigningKey.generate()  # 生成私鑰
    public_key = private_key.get_verifying_key()  # 從私鑰獲取公鑰

    # 將消息進行 SHA-256 哈希
    hashed_message = hashlib.sha256(message.encode()).hexdigest()

    # 使用私鑰對哈希值進行簽名
    signature = private_key.sign(hashed_message.encode())

    return render_template('result.html', message=message, public_key=public_key, signature=signature)

if __name__ == '__main__':
    app.run(debug=True)
