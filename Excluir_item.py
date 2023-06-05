from tkinter import *


janela = Tk()
janela.title("Alteração de item")
janela.geometry('500x300+350+200')
rotulo = Label(janela, font="Arial 18 bold", text='Exclusão de item')
rotulo.place(x=25, y=10)

rotulo = Label(janela, font="Arial 10", text='Código')
rotulo.place(x=25, y=67)
cxtexto1 = Entry(janela, width=10)
cxtexto1.place(x=90, y=67)

bt2 = Button(janela, width=10, text="Pesquisar", font="Arial 10 bold")
bt2.place(x=160, y=62)



rotulo = Label(janela, font="Arial 10", text='Descrição')
rotulo.place(x=25, y=100)
cxtexto2 = Entry(janela, width=30)
cxtexto2.place(x=90, y=100)

rotulo = Label(janela, font="Arial 10", text='Valor')
rotulo.place(x=25, y=130)
cxtexto3 = Entry(janela, width=20)
cxtexto3.place(x=90, y=130)

rotulo = Label(janela, font="Arial 10", text='Obs.')
rotulo.place(x=25, y=160)
cxtexto4 = Entry(janela, width=50)
cxtexto4.place(x=90, y=160)

bt3 = Button(janela, width=10, text="Fechar", font="Arial 12 bold", command=janela.destroy)
bt3.place(x=260, y=230)

bt4 = Button(janela, width=10, text="Excluir", font="Arial 12 bold")
bt4.place(x=130, y=230)


lblmsg = Label(janela, font="Arial 10", text='Obs.')
lblmsg.place(x=25, y=160)





janela.mainloop()