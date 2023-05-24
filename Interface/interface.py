# Importando a Biblioteca 
import tkinter 

# Criando a janela 
janela = tkinter.Tk()

# Tamanho da janela 
janela.geometry("300x300")

# Atribuindo um título 
janela.title("Pimeira Interface com Python")


# Colocando um texto dentro da janela 
texto = tkinter.Label(janela, text="Olá mundo!")
# Exibindo o texto na janela 
texto.pack()

# Exibindo a tela 
janela.mainloop()