from flask import Flask, request, render_template
import hashlib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hash', methods=['POST'])
def hash_text():
    text = request.form['text']
    hash_result = hashlib.sha256(text.encode()).hexdigest()
    return render_template('hash_result.html', text=text, hash_result=hash_result)

@app.route('/sha256', methods=['POST'])
def sha256_text():
    text = request.form['text']
    sha256_result = hashlib.sha256(text.encode()).hexdigest()
    return render_template('sha256_result.html', text=text, sha256_result=sha256_result)

if __name__ == '__main__':
    app.run(debug=True)
