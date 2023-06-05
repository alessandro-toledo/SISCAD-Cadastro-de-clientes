from tkinter import *

def avisoSucesso():
    janela = Toplevel()
    janela.title("Aviso")
    janela.geometry('300x200+500+250')
    #imagem = PhotoImage(file ="C:/Users/Usuario/Desktop/Sistema novo/alert.png")
    #rotulo1 = Label(janela5, text='imagem', image=imagem)
    #rotulo1.place(x=70, y=70)
    rotulo = Label(janela, font="Arial 20 bold", text='Operação realizada com sucesso')
    rotulo.place(x=85, y=100)
    botao = Button(janela, width=10, text="OK", font="Arial 10 bold", command=janela.destroy)
    botao.place(x=105, y=150)

