from email.mime import image
import qrcode 

image = qrcode.make("https://github.com/Anaportfolio/QR-Code")
image.save("primeiro_qrcode.jpg")