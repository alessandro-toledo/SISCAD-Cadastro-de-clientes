import sqlite3

def cria_bd(coditem, descr, valor, obs):
    conn = sqlite3.connect('itembd.db')
    bd = conn.cursor()
    bd.execute("""CREATE TABLE IF NOT EXISTS Itens (
        
        Coditem INT NOT NULL PRIMARY KEY,
        Descr TEXT NOT NULL,
        Valor TEXT NOT NULL,
        Obs TEXT NOT NULL);""")

    bd.execute("""INSERT INTO Itens (Coditem, Descr, Valor, Obs) VALUES (?,?,?,?);""", (coditem, descr, valor, obs))
    conn.commit()
    conn.close()

con = sqlite3.connect("itembd.db")

def selecionar(i):
    lista_tarefa=[]
    with con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Itens WHERE Coditem = {i}")
        row = cur.fetchall()
        for r in row:
            lista_tarefa.append(r)
    return lista_tarefa

def alterar(d, i, v, o):
    with con:
        cur = con.cursor()
        cur.execute(f"UPDATE Itens SET (Descr, Valor, Obs) = (?,?,?) WHERE Coditem = ?", (d, v, o, i))

def deletar(i):    
    with con:
        cur = con.cursor()
        cur.execute(f"DELETE FROM Itens WHERE Coditem={i}")

def selecionar1():
    lista_tarefa=[]
    with con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Itens")
        row = cur.fetchall()
        for r in row:
            lista_tarefa.append(r)
    return lista_tarefa
        
def deletar1():    
    with con:
        cur = con.cursor()
        cur.execute(f"DELETE FROM Itens WHERE Coditem=''")

#i = 123
#deletar(i)

#d = 'Namoradeira de junco'
#i = 123
#v = 10.56
#o = 'Nova observação'
#alterar(d,i,v,o)

#print (selecionar(123))

#### IMPORTANTE: 
#i = 1020



#t = (selecionar1())
#print(t)

#deletar1()
#if t == None:
#    print ("Não achei")
#else:
#    print("Achei")