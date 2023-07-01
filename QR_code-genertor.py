# install all the library needed 
# create a function that collects a test and converts it to a qrcode
# save the qrcode as a image
import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size= 10,
        border= 4

    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color = "white")
    img.save("qring.png")
url = input("Enter your url to create qr: ")
generate_qrcode("url")

    