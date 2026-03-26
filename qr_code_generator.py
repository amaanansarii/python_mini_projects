import qrcode as qr
from PIL import Image

url = "https://github.com/amaanansarii"

img = qr.make(url) # generate the image of qr of this particular link
img.save("amaan_github.png") # save the image in same forlder in png format

new_qr = qr.QRCode(version=1,
                    error_correction=qr.constants.ERROR_CORRECT_H,
                    box_size=10, border=4,)


new_qr.add_data(url)
new_qr.make(fit=True)

image=new_qr.make_image(fill_color="red", back_color="blue")
image.save("amaanNew_github.png")
