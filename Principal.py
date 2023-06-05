from tkinter import *
import item

def abrir():
    janela3 = Toplevel(janela2)
    
    def salvar():
        coditem = cxtexto1.get()
        descr = cxtexto2.get()
        valor = cxtexto3.get()
        obs = cxtexto4.get()
        janela6 = Toplevel(janela3)
        janela6.title("Aviso")
        janela6.geometry('400x200+500+250')
        janela6.resizable(width=False, height=False)
        
        try:
            valor = valor
        except:
            msg_erro = "erro"
        else:
            msg_erro = ""
        if coditem == "" or descr == "" or valor == "":
            mensagem = "RG, Nome e Endereço devem ser preenchidos"
        
        elif msg_erro == "erro":
            mensagem = "O campo 'email' deve ser preenchido"
        else:
            item.cria_bd(coditem, descr, valor, obs)
            mensagem = "Operação realizada com sucesso"
            cxtexto1.delete(0, END)
            cxtexto2.delete(0, END)
            cxtexto3.delete(0, END)
            cxtexto4.delete(0, END)
            cxtexto1.focus()
        rotulo = Label(janela6, font="Arial 10 bold", text=mensagem, anchor="center", width=48)
        rotulo.place(x=0, y=100)
        botao = Button(janela6, width=10, text="OK", font="Arial 10 bold", command=janela6.destroy)
        botao.place(x=155, y=150)    
               
    janela3.title("Cadastro de item")
    janela3.geometry('500x280+350+200')
    rotulo = Label(janela3, font="Arial 18 bold", text='Cadastro de Cliente')
    rotulo.place(x=25, y=10)

    rotulo = Label(janela3, font="Arial 10", text='RG')
    rotulo.place(x=25, y=70)
    cxtexto1 = Entry(janela3, width=30)
    cxtexto1.place(x=90, y=70)
    janela3.resizable(width=False, height=False)

    rotulo = Label(janela3, font="Arial 10", text='Nome')
    rotulo.place(x=25, y=100)
    cxtexto2 = Entry(janela3, width=60)
    cxtexto2.place(x=90, y=100)

    rotulo = Label(janela3, font="Arial 10", text='Endereço')
    rotulo.place(x=25, y=130)
    cxtexto3 = Entry(janela3, width=60)
    cxtexto3.place(x=90, y=130)
    valor = cxtexto3.get()
        
    rotulo = Label(janela3, font="Arial 10", text='email')
    rotulo.place(x=25, y=160)
    cxtexto4 = Entry(janela3, width=60)
    cxtexto4.place(x=90, y=160)
    
    bt2 = Button(janela3, width=10, text="Salvar", font="Arial 12 bold", command=salvar)
    bt2.place(x=140, y=220)
    bt3 = Button(janela3, width=10, text="Fechar", font="Arial 12 bold", command=janela3.destroy)
    bt3.place(x=260, y=220)


def consultar():
    janela4 = Toplevel(janela2)

    def pesquisar():
        it = item
        try:
            coditem = cxtexto1.get()
            cxtexto2.delete(0, END)
            cxtexto2.insert(INSERT,it.selecionar(coditem)[0][1])
            cxtexto3.delete(0, END)
            cxtexto3.insert(INSERT,it.selecionar(coditem)[0][2])
            cxtexto4.delete(0, END)
            cxtexto4.insert(INSERT,it.selecionar(coditem)[0][3])
        except:
            janela5 = Toplevel(janela4)
            janela5.title("Aviso")
            janela5.geometry('300x200+500+250')
            rotulo = Label(janela5, font="Arial 10 bold", text='Cadastro não localizado')
            rotulo.place(x=85, y=100)
            botao = Button(janela5, width=10, text="OK", font="Arial 10 bold", command=janela5.destroy)
            botao.place(x=105, y=150)

    def limpar():
        cxtexto1.delete(0, END)
        cxtexto2.delete(0, END)
        cxtexto3.delete(0, END)
        cxtexto4.delete(0, END)

    def consultar_alterar():
        con_transf = cxtexto1.get()
        alterar()
        cxtexto1.insert(INSERT,con_transf)

    janela4.title("Pesquisa de item")
    janela4.geometry('500x300+350+200')
    rotulo = Label(janela4, font="Arial 18 bold", text='Pesquisa de Cadastro')
    rotulo.place(x=25, y=10)
    janela4.resizable(width=False, height=False)

    rotulo = Label(janela4, font="Arial 10", text='RG')
    rotulo.place(x=25, y=67)
    cxtexto1 = Entry(janela4, width=10)
    cxtexto1.place(x=90, y=67)

    bt2 = Button(janela4, width=10, text="Pesquisar", font="Arial 10 bold",command=pesquisar)
    bt2.place(x=160, y=62)

    rotulo = Label(janela4, font="Arial 10", text='Nome')
    rotulo.place(x=25, y=100)
    cxtexto2 = Entry(janela4, width=60)
    cxtexto2.place(x=90, y=100)
    
    rotulo = Label(janela4, font="Arial 10", text='Endereço')
    rotulo.place(x=25, y=130)
    cxtexto3 = Entry(janela4, width=60)
    cxtexto3.place(x=90, y=130)

    rotulo = Label(janela4, font="Arial 10", text='email')
    rotulo.place(x=25, y=160)
    cxtexto4 = Entry(janela4, width=60)
    cxtexto4.place(x=90, y=160)

    bt3 = Button(janela4, width=10, text="Fechar", font="Arial 10 bold", command=janela4.destroy)
    bt3.place(x=350, y=230)

    #bt4 = Button(janela4, width=15, text="Alterar este Cadastro", font="Arial 10 bold", command=consultar_alterar)
    #bt4.place(x=205, y=230)

    bt5 = Button(janela4, width=15, text="Limpar pesquisa", font="Arial 10 bold", command=limpar)
    bt5.place(x=60, y=230)


    lblmsg = Label(janela4, font="Arial 10", text='Obs.')
    lblmsg.place(x=25, y=160)


def alterar():
    janela5 = Toplevel(janela2)

    def alterar1():
        i = cxtexto1.get()
        d = cxtexto5.get()
        v = cxtexto6.get()
        o = cxtexto7.get()
        item.alterar(d, i, v, o)
        cxtexto1.delete(0, END)
        cxtexto2.delete(0, END)
        cxtexto3.delete(0, END)
        cxtexto4.delete(0, END)
        cxtexto5.delete(0, END)
        cxtexto6.delete(0, END)
        cxtexto7.delete(0, END)
        janela6 = Toplevel(janela5)
        janela6.title("Aviso")
        janela6.geometry('300x200+500+250')
        rotulo = Label(janela6, font="Arial 10 bold", text='Operação realizada com sucesso')
        rotulo.place(x=43, y=100)
        
        botao = Button(janela6, width=10, text="OK", font="Arial 10 bold", command=janela6.destroy)
        botao.place(x=105, y=150)        

    def pesquisar():
        it = item
        try:
            coditem = cxtexto1.get()
            cxtexto2.delete(0, END)
            cxtexto2.insert(INSERT,it.selecionar(coditem)[0][1])
            cxtexto3.delete(0, END)
            cxtexto3.insert(INSERT,it.selecionar(coditem)[0][2])
            cxtexto4.delete(0, END)
            cxtexto4.insert(INSERT,it.selecionar(coditem)[0][3])
        except:
            janela6 = Toplevel(janela5)
            janela6.title("Aviso")
            janela6.geometry('300x200+500+250')
            rotulo = Label(janela6, font="Arial 10 bold", text='Cadastro não localizado')
            rotulo.place(x=85, y=100)
            botao = Button(janela6, width=10, text="OK", font="Arial 10 bold", command=janela6.destroy)
            botao.place(x=105, y=150)

    def limpar():
        cxtexto1.delete(0, END)
        cxtexto2.delete(0, END)
        cxtexto3.delete(0, END)
        cxtexto4.delete(0, END)

    janela5.title("Alteração de cadastro")
    janela5.geometry('800x350+350+200')
    rotulo = Label(janela5, font="Arial 18 bold", text='Alteração de Cadastro')
    rotulo.place(x=25, y=10)
    janela5.resizable(width=False, height=False)

    rotulo = Label(janela5, font="Arial 10", text='RG')
    rotulo.place(x=25, y=67)
    cxtexto1 = Entry(janela5, width=10)
    cxtexto1.place(x=90, y=67)

    bt2 = Button(janela5, width=10, text="Pesquisar", font="Arial 10 bold", command=pesquisar)
    bt2.place(x=160, y=62)

    rotulo = Label(janela5, font="Arial 9 italic bold", text="Informações Antigas:", fg="blue")
    rotulo.place(x=25, y=103)

    rotulo = Label(janela5, font="Arial 9 italic bold", text="Informações Novas:")
    rotulo.place(x=25, y=193)

    rotulo = Label(janela5, font="Arial 10", text='Nome', fg="blue")
    rotulo.place(x=25, y=130)
    cxtexto2 = Entry(janela5, width=50, fg="blue")
    cxtexto2.place(x=90, y=130)

    rotulo = Label(janela5, font="Arial 10", text='Endereço', fg="blue")
    rotulo.place(x=400, y=130)
    cxtexto3 = Entry(janela5, width=50, fg="blue")
    cxtexto3.place(x=460, y=130)

    rotulo = Label(janela5, font="Arial 10", text='email', fg="blue")
    rotulo.place(x=25, y=160)
    cxtexto4 = Entry(janela5, width=50, fg="blue")
    cxtexto4.place(x=90, y=160)

    #Novos valores######################################################
    rotulo = Label(janela5, font="Arial 10", text='Nome')
    rotulo.place(x=25, y=220)
    cxtexto5 = Entry(janela5, width=50)
    cxtexto5.place(x=90, y=220)

    rotulo = Label(janela5, font="Arial 10", text='Endereço')
    rotulo.place(x=400, y=220)
    cxtexto6 = Entry(janela5, width=50)
    cxtexto6.place(x=460, y=220)

    rotulo = Label(janela5, font="Arial 10", text='email')
    rotulo.place(x=25, y=250)
    cxtexto7 = Entry(janela5, width=50)
    cxtexto7.place(x=90, y=250)
    #Encerra aqui######################################################

    bt3 = Button(janela5, width=10, text="Fechar", font="Arial 12 bold", command=janela5.destroy)
    bt3.place(x=260, y=300)

    bt4 = Button(janela5, width=10, text="Alterar", font="Arial 12 bold", command=alterar1)
    bt4.place(x=130, y=300)

def excluir():
    janela6 = Toplevel(janela2)

    def pesquisar():
        it = item
        try:
            coditem = cxtexto1.get()
            cxtexto2.delete(0, END)
            cxtexto2.insert(INSERT,it.selecionar(coditem)[0][1])
            cxtexto3.delete(0, END)
            cxtexto3.insert(INSERT,it.selecionar(coditem)[0][2])
            cxtexto4.delete(0, END)
            cxtexto4.insert(INSERT,it.selecionar(coditem)[0][3])
        except:
            janela7 = Toplevel(janela6)
            janela7.title("Aviso")
            janela7.geometry('300x200+500+250')
            rotulo = Label(janela7, font="Arial 10 bold", text='Cadastro não localizado')
            rotulo.place(x=85, y=100)
            botao = Button(janela7, width=10, text="OK", font="Arial 10 bold", command=janela7.destroy)
            botao.place(x=105, y=150)
        
    def excluir():
        i = cxtexto1.get()

        def botaoexcluir():
            item.deletar(i)
            cxtexto1.delete(0, END)
            cxtexto2.delete(0, END)
            cxtexto3.delete(0, END)
            cxtexto4.delete(0, END)
            janela7.after(1,janela7.destroy)
            rotulo = Label(janela6, font="Arial 16 bold", fg="green", text="Cadastro excluído com sucesso")
            rotulo.place(x=112, y=200)
        
        janela7 = Toplevel(janela6)
        janela7.title("Aviso")
        janela7.geometry('300x200+500+250')
        rotulo = Label(janela7, font="Arial 10 bold", text='Tem certeza?')
        rotulo.place(x=85, y=100)
        Button(janela7, width=10, text="Sim", font="Arial 10 bold", command=botaoexcluir).place(x=50, y=150)
        Button(janela7, width=10, text="Não", font="Arial 10 bold", command=janela7.destroy).place(x=150, y=150)
        janela7.resizable(width=False, height=False)

    janela6.title("Exclusão de item")
    janela6.geometry('500x300+350+200')
    rotulo = Label(janela6, font="Arial 18 bold", text='Exclusão de Cadastro')
    rotulo.place(x=25, y=10)
    janela6.resizable(width=False, height=False)

    rotulo = Label(janela6, font="Arial 10", text='RG')
    rotulo.place(x=25, y=67)
    cxtexto1 = Entry(janela6, width=10)
    cxtexto1.place(x=90, y=67)

    bt2 = Button(janela6, width=10, text="Pesquisar", font="Arial 10 bold", command=pesquisar)
    bt2.place(x=160, y=62)

    rotulo = Label(janela6, font="Arial 10", text='Nome')
    rotulo.place(x=25, y=100)
    cxtexto2 = Entry(janela6, width=60)
    cxtexto2.place(x=90, y=100)

    rotulo = Label(janela6, font="Arial 10", text='Endereço')
    rotulo.place(x=25, y=130)
    cxtexto3 = Entry(janela6, width=60)
    cxtexto3.place(x=90, y=130)

    rotulo = Label(janela6, font="Arial 10", text='email')
    rotulo.place(x=25, y=160)
    cxtexto4 = Entry(janela6, width=60)
    cxtexto4.place(x=90, y=160)

    bt3 = Button(janela6, width=10, text="Fechar", font="Arial 12 bold", command=janela6.destroy)
    bt3.place(x=260, y=250)
    bt4 = Button(janela6, width=10, text="Excluir", font="Arial 12 bold", command=excluir)
    bt4.place(x=130, y=250)

janela2 = Tk()
janela2.title("Controle de Cadastros")
janela2.geometry('800x600+350+200')
janela2.state('zoomed') #Inicia a janela maximizada automaticamente

frame00000 = Frame(janela2, padx=1, pady=10)
frame00000.pack()
frame_1 = Frame(frame00000, padx=1, pady=1)
frame_1.pack()
frame0 = Frame(janela2, padx=5, pady=5)
frame0.pack()
frame00 = Frame(janela2, padx=5, pady=5)
frame00.pack()
frame000 = Frame(janela2, padx=5, pady=5)
frame000.pack()
frame0000 = Frame(janela2, padx=5, pady=5)
frame0000.pack()
frame1 = Frame(frame0, highlightbackground="grey", highlightthickness=1, padx=10, pady=10)
frame1.pack()
frame2 = Frame(frame00, highlightbackground="grey", highlightthickness=1, padx=136, pady=10)
frame2.pack()
frame3 = Frame(frame000, highlightbackground="grey", highlightthickness=1, padx=10, pady=10)
frame3.pack()
frame4 = Frame(frame0000, highlightbackground="grey", highlightthickness=1, padx=199, pady=10)
frame4.pack()

acesso = Label(frame_1, text="Acesso rápido", font="Arial 9 italic", fg="grey")
acesso.pack(side=LEFT)
bt2 = Button(frame1, text="Cadastrar cliente", width=14, padx=10, pady=10, command=abrir)
bt2.pack(side=LEFT)
bt3 = Button(frame1, width=14, text="Consultar cliente",padx=10, pady=10, command=consultar)
bt3.pack(side=LEFT)
bt4 = Button(frame1, width=14, text="Alterar cliente", padx=10, pady=10, command=alterar)
bt4.pack(side=LEFT)
bt4 = Button(frame1, width=14, text="Excluir cliente", padx=10, pady=10, command=excluir)
bt4.pack(side=LEFT)
#bt5 = Button(frame2, width=14, text="Consultar cliente",padx=10, pady=10)
#bt5.pack(side=LEFT)
#bt6 = Button(frame2, width=14, text="Alterar estoque",padx=10, pady=10)
#bt6.pack(side=LEFT)
#bt7 = Button(frame3, width=14, text="Gerar nota",padx=10, pady=10)
#bt7.pack(side=LEFT)
#bt8 = Button(frame3, width=14, text="Consultar nota",padx=10, pady=10)
#bt8.pack(side=LEFT)
#bt9 = Button(frame3, width=14, text="Alterar nota",padx=10, pady=10)
#bt9.pack(side=LEFT)
#bt10 = Button(frame3, width=14, text="Excluir nota",padx=10, pady=10)
#bt10.pack(side=LEFT)
#bt11 = Button(frame4, width=14, text="Relatório",padx=10, pady=10)
#bt11.pack(side=LEFT)

# Código dos menus

menubar = Menu(janela2)
filemenu = Menu(menubar)
filemenu.add_command(label="Cadastrar", command=abrir)
filemenu.add_command(label="Consultar", command=consultar)
filemenu.add_command(label="Alterar", command=alterar)
filemenu.add_command(label="Excluir", command=excluir)
menubar.add_cascade(label="Cadastro de clientes", menu=filemenu)
#filemenu1 = Menu(menubar)
#filemenu1.add_command(label="Consultar")
#filemenu1.add_command(label="Alterar")
#filemenu1.add_command(label="Imprimir")
#filemenu1.add_command(label="Exportar")
#menubar.add_cascade(label="Estoque", menu=filemenu1)
#filemenu2 = Menu(menubar)
#filemenu2.add_command(label="Nova")
#filemenu2.add_command(label="Consultar")
#filemenu2.add_command(label="Alterar")
#filemenu2.add_command(label="Excluir")
#ilemenu2.add_command(label="Imprimir")
#menubar.add_cascade(label="Nota", menu=filemenu2)
#filemenu3 = Menu(menubar)
#filemenu3.add_command(label="Estoque")
#filemenu3.add_command(label="Itens")
#filemenu3.add_command(label="Período")
#menubar.add_cascade(label="Relatórios", menu=filemenu3)
#filemenu4 = Menu(menubar)
#filemenu4.add_command(label="Usuário")
#filemenu4.add_command(label="Empresa")
#menubar.add_cascade(label="Cadastros", menu=filemenu4)
#filemenu5 = Menu(menubar)
#filemenu5.add_command(label="Sair", command=janela2.quit)
#menubar.add_cascade(label="Sair", menu=filemenu5)
janela2.config(menu=menubar)

janela2.mainloop()