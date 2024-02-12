import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image, ImageOps, ImageDraw

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

def add_background(img, color):
    bg = Image.new('RGB', img.size, color)
    bg.paste(img, (0, 0))
    return bg

#qr = qrcode.QRCode()
qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=5,border=0,image_factory=StyledPilImage)

qr.add_data('https://www.linkedin.com/in/alexis-f-7726a168')
qr.make(fit=True)
img = qr.make_image(fill_color="#536c80", back_color="white", module_drawer=CircleModuleDrawer(), color_mask=SolidFillColorMask(front_color=(83, 108, 128))).convert('RGB')

logo = Image.open('logo/linkedin.png')
#logo=logo.resize((50,50),Image.ANTIALIAS)
logo.thumbnail((50, 50), Image.ANTIALIAS)
#logo=add_corners(logo, 5)
#logo = add_background(logo, "white")
#logo.save('testlogo.png')

logo_display = ImageOps.expand(logo, border=(5, 5, 5, 5), fill="white")

logo_pos = ((img.size[0] - logo_display.size[0]) // 2, (img.size[1] - logo_display.size[1]) // 2)
img.paste(logo_display, logo_pos)
#img = add_background(img, (255, 255, 255))
img.save("QR.png")
