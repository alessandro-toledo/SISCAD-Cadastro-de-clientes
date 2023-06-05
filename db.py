import sqlite3 as lite

con = lite.connect("lista.db")

#with con:
 #   cur= con.cursor()
  #  cur.execute("CREATE TABLE tarefa (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)")

def inserir(i):
    with con:
        cur= con.cursor()
        query = "INSERT INTO tarefa (nome) VALUES (?)"
        cur.execute(query, i)

def selecionar():
    lista_tarefa=[]
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tarefa")
        row = cur.fetchall()
        for r in row:
            lista_tarefa.append(r)
    return lista_tarefa

def deletar(i):    
    with con:
        cur = con.cursor()
        query = "DELETE FROM tarefa WHERE id=?"
        cur.execute(query, i)

def atualizar(i):
    with con:
        cur = con.cursor()
        query = "UPDATE tarefa SET nome='Comer' WHERE id=?"
        cur.execute(query, i)