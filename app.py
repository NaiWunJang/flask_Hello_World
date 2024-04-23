from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

def calculate_hash(data):
    # 使用SHA-256算法計算哈希值
    hash_object = hashlib.sha256(data.encode())
    # 返回十六進制表示的哈希值
    return hash_object.hexdigest()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # 從表單中獲取用戶輸入的數據
        data = request.form["data"]
        # 計算哈希值
        hashed_data = calculate_hash(data)
        # 將計算結果顯示在模板中
        return render_template("result.html", data=data, hashed_data=hashed_data)
    # 如果是GET請求，顯示首頁
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
