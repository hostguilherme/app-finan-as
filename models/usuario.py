# models/usuario.py
import sqlite3
from db.database import Database

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha  

    def salvar_no_banco(self):
        conn = sqlite3.connect('financas.db')
        c = conn.cursor()
        c.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)',
                  (self.nome, self.email, self.senha))
        conn.commit()
        conn.close()

    @staticmethod
    def buscar_por_email(email):
        conn = sqlite3.connect('financas.db')
        c = conn.cursor()
        c.execute('SELECT * FROM usuarios WHERE email = ?', (email,))
        usuario = c.fetchone()
        conn.close()
        if usuario:
            return Usuario(usuario[1], usuario[2], usuario[3]) 
        else:
            return None

    @staticmethod
    def login(email, senha):
        conn = sqlite3.connect('financas.db')
        c = conn.cursor()
        c.execute('SELECT * FROM usuarios WHERE email = ? AND senha = ?', (email, senha))
        usuario = c.fetchone()
        conn.close()
        if usuario:
            return usuario
        else:
            print("Credenciais inválidas.")
            return None

    @classmethod
    def cadastrar(cls):
        db = Database()
        db.criar_tabelas()

        print("Cadastro de Novo Usuário")
        nome = input("Digite seu nome: ")
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")

        novo_usuario = cls(nome, email, senha)
        novo_usuario.salvar_no_banco()
        print("Usuário cadastrado com sucesso!")

    @classmethod
    def fazer_login(cls):
        print("Login")
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")

        usuario_logado = cls.login(email, senha)
        if usuario_logado:
            return usuario_logado  # Retorna a tupla contendo (id, nome) do usuário
        else:
            print("Credenciais inválidas.")
            return None

