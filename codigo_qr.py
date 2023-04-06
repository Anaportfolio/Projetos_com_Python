from email.mime import image
import qrcode 

link = input ("Digite o link: ")
image = qrcode.make(link)
image.save("segundo_qrcode.jpg")