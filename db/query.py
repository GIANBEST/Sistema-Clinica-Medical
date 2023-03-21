import sqlite3

class server_db:
    
    def __init__(self,server =None): #este código cria banco de dados em sqlite
        self.conn = None
        self.cursor = None

        if server:
            self.open(server)
    
    
    def open(self,server):
        try:
            self.conn = sqlite3.connect(server)
            self.cursor = self.conn.cursor()
            print("Conexão foi completada com sucesso")
        except sqlite3.Error as e:
            print("Conexão Falhou")


    def criar_tabelas(self):
        cur = self.cursor
        cur.execute("""CREATE TABLE funcs(
        id INTEGER PRIMARY KEY autoincrement,
        nome text NOT NULL,
        endereço text NOT NULL,
        documento integer NOT NULL,
        admin integer)""")



db = server_db("fun.db")

db.criar_tabelas()