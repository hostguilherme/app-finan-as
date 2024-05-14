import sqlite3
from db.database import Database
from datetime import datetime

class Renda:
    def __init__(self, user_id, valor, descricao, data, hora):
        self.user_id = user_id
        self.valor = valor
        self.descricao = descricao
        self.data = data
        self.hora = hora

    def salvar_no_banco(self):
        conn = sqlite3.connect('financas.db')
        c = conn.cursor()
        c.execute('INSERT INTO renda (user_id, valor, descricao, data, hora) VALUES (?, ?, ?, ?, ?)',
                  (self.user_id, self.valor, self.descricao, self.data, self.hora))
        conn.commit()
        conn.close()

    @classmethod
    def adicionar_renda(cls, user_id):
        print("Adicionar Renda")
        valor = float(input("Digite o valor da renda: "))
        descricao = input("Digite uma descrição para a renda: ")
        data = datetime.now().strftime("%Y-%m-%d")
        hora = datetime.now().strftime("%H:%M:%S")

        nova_renda = cls(user_id, valor, descricao, data, hora)
        nova_renda.salvar_no_banco()
        print("Renda adicionada com sucesso!")
