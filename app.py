from flask import Flask, render_template, request, send_file
import qrcode 
import os

app = Flask(__name__)

QR_FOLDER = "qr_codes"

if not os.path.exists(QR_FOLDER):
    os.makedirs(QR_FOLDER)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form['data']
    filename = f"{QR_FOLDER}/qr.png"

    img = qrcode.make(data)
    img.save(filename)

    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)