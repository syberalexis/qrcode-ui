import qrcode
import qrcode.image.svg
from PIL import Image

def generate_qr_with_logo(data, logo_path, output_path):
    # Générer le QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Créer une image QR code
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Ouvrir le logo et le redimensionner
    logo = Image.open(logo_path)
    logo_width, logo_height = logo.size
    qr_img_width, qr_img_height = qr_img.size
    logo_size = int(qr_img_width / 4)

    # Calculer la position du logo
    position = ((qr_img_width - logo_size) // 2, (qr_img_height - logo_size) // 2)

    # Coller le logo sur l'image QR code
    qr_img.paste(logo.resize((logo_size, logo_size), Image.ANTIALIAS), position)

    # Enregistrer l'image finale
    qr_img.save(output_path)

def generate_qr_svg(data, logo_path, output_path):
    qr = qrcode.QRCode(image_factory=qrcode.image.svg.SvgPathImage)
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image()

    # Ouvrir le logo et le redimensionner
    logo = Image.open(logo_path)
    logo_width, logo_height = logo.size
    qr_img_width, qr_img_height = (10, 10)
    logo_size = int(qr_img_width / 4)

    # Calculer la position du logo
    position = ((qr_img_width - logo_size) // 2, (qr_img_height - logo_size) // 2)

    # Coller le logo sur l'image QR code
    qr_img.paste(logo.resize((logo_size, logo_size), Image.ANTIALIAS), position)


    qr_img.save(output_path)


if __name__ == "__main__":
    # Data pour le QR code
    data = "https://www.linkedin.com"

    # Chemin du logo
    logo_path = "logo/linkedin.png"

    # Générer le QR code avec le logo
    # generate_qr_with_logo(data, logo_path, "test.png")
    generate_qr_svg(data, logo_path, "test.svg")
