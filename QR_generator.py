# install the libraries needed
#create a function that collects a text adn converts it to a QR Code
#save the QR code as an image

from asyncio import constants
from turtle import fillcolor
import qrcode

def generate_qrcode(text):
    
    qr = qrcode.QRCode(
        version = 1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg001.png")


url = input("Enter the URL:  ")
generate_qrcode(url)

