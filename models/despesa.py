import sqlite3
from db.database import Database

class Despesa:
    @classmethod
    def adicionar_despesa(cls, user_id, categoria, valor, descricao, data, hora):
        conn = sqlite3.connect('financas.db')
        c = conn.cursor()
        c.execute('''INSERT INTO despesa (user_id, categoria, valor, descricao, data, hora) 
                     VALUES (?, ?, ?, ?, ?, ?)''', (user_id, categoria, valor, descricao, data, hora))
        conn.commit()
        conn.close()

    @classmethod
    def remover_despesa(cls, despesa_id):
        conn = sqlite3.connect('financas.db')
        c = conn.cursor()
        c.execute('DELETE FROM despesa WHERE id = ?', (despesa_id,))
        conn.commit()
        conn.close()

    @classmethod
    def visualizar_despesas(cls, user_id):
        conn = sqlite3.connect('financas.db')
        c = conn.cursor()
        c.execute('SELECT * FROM despesa WHERE user_id = ?', (user_id,))
        despesas = c.fetchall()
        conn.close()
        return despesas
