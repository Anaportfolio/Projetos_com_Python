from email.mime import image
import qrcode 

link = input ("Digite o link: ")
text = input("Digite o nome que deseja salvar: ")
image = qrcode.make(link)
image.save(text +".jpg")