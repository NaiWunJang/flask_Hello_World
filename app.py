from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 存儲留言的列表，這個列表將在服務器重啟時丟失
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/post', methods=['POST'])
def post():
    author = request.form['author']
    content = request.form['content']
    messages.append({'author': author, 'content': content})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
