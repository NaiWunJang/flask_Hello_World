from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def create_table():
    conn = sqlite3.connect('messages.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS messages
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                author TEXT,
                content TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('messages.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM messages''')
    messages = cur.fetchall()
    conn.close()
    return render_template('index.html', messages=messages)

@app.route('/post', methods=['POST'])
def post():
    author = request.form['author']
    content = request.form['content']
    conn = sqlite3.connect('messages.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO messages (author, content) VALUES (?, ?)''', (author, content))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
