from flask import Flask, render_template

app = Flask(__name__)

# 首頁
@app.route('/')
def index():
    return render_template('index.html')

# 文章頁面
@app.route('/post/<int:post_id>')
def post(post_id):
    # 這裡可以添加從數據庫中獲取特定文章的邏輯
    # 例如，你可以從數據庫中根據 post_id 獲取文章的標題、內容等信息
    # 在這個示例中，我們直接將 post_id 傳遞給模板
    return render_template('post.html', post_id=post_id)

# 關於頁面
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
