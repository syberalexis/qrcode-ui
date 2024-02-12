from flask import Flask, render_template, request, send_file
import qrcode
from PIL import Image

app = Flask(__name__)

def generate_qr_logo(data, logo_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")

    logo = Image.open(logo_path)
    logo_width, logo_height = logo.size
    qr_img_width, qr_img_height = qr_img.size
    logo_size = int(qr_img_width / 4)

    position = ((qr_img_width - logo_size) // 2, (qr_img_height - logo_size) // 2)

    qr_img.paste(logo.resize((logo_size, logo_size), Image.ANTIALIAS), position)

    return qr_img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form['data']
    logo = request.files['logo']
    logo.save(logo.filename)

    qr_img = generate_qr_logo(data, logo.filename)
    qr_img.save('qrcode_with_logo.png')

    return send_file('qrcode_with_logo.png', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
