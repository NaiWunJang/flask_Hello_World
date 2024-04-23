from flask import Flask, render_template, request
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hash', methods=['POST'])
def hash():
    text = request.form.get('text')
    hashed_text = hashlib.sha256(text.encode()).hexdigest()
    return render_template('result.html', title='Cryptographic Hash Function', text=text, hashed_text=hashed_text)

@app.route('/sha256', methods=['POST'])
def sha256():
    text = request.form.get('text')
    hashed_text = hashlib.sha256(text.encode()).hexdigest()
    return render_template('result.html', title='SHA-256 Hash Function', text=text, hashed_text=hashed_text)

if __name__ == '__main__':
    app.run(debug=True)
