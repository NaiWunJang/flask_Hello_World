from flask import Flask, request, render_template
import hashlib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hash_text():
    md5_hash = None
    sha256_hash = None

    if request.method == 'POST':
        text = request.form['text']
        md5_hash = hashlib.md5(text.encode()).hexdigest()
        sha256_hash = hashlib.sha256(text.encode()).hexdigest()

    return render_template('index.html', md5_hash=md5_hash, sha256_hash=sha256_hash)

if __name__ == '__main__':
    app.run(debug=True)
