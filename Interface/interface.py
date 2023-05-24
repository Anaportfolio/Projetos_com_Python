# Importando a Biblioteca 
from tkinter import*

# Criando a janela 
janela = Tk()

# Tamanho da janela 
janela.geometry("300x300")

# Atribuindo um título 
janela.title("Pimeira Interface com Python")


# Colocando um texto dentro da janela 
texto =Label(janela, text="Olá mundo!")
# Exibindo o texto na janela 
texto.pack()


# Exibindo a tela 
janela.mainloop()