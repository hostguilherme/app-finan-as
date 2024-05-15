import sqlite3

class Database:
    def __init__(self, db_name='financas.db'):
        self.db_name = db_name

    def criar_tabelas(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                     id INTEGER PRIMARY KEY,
                     nome TEXT NOT NULL,
                     email TEXT UNIQUE NOT NULL,
                     senha TEXT NOT NULL)''')

        c.execute('''CREATE TABLE IF NOT EXISTS renda (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     user_id INTEGER,
                     valor FLOAT,
                     descricao VARCHAR(200),
                     data TEXT,
                     hora TEXT,
                     FOREIGN KEY (user_id) REFERENCES usuarios(id))''')
                     
        c.execute('''CREATE TABLE IF NOT EXISTS despesa (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     user_id INTEGER,
                     categoria TEXT VARCHAR(45),
                     valor FLOAT,
                     descricao VARCHAR(200),
                     data TEXT,
                     hora TEXT,
                     FOREIGN KEY (user_id) REFERENCES usuarios(id))''')


        conn.commit()
        conn.close()
