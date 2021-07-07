import sqlite3
from prettytable import from_db_cursor

def criar_banco():
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pessoas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                endereco TEXT NOT NULL,
                cpf TEXT NOT NULL)''')
    conexao.close()

def cadastrar(nome, endereco, cpf):
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()
    valores = nome, endereco, cpf
    sql = 'INSERT INTO pessoas(nome, endereco, cpf) VALUES (?, ?, ?)'
    cursor.execute(sql, valores)
    conexao.commit()
    conexao.close

def relatorio():
    conexao = sqlite3.connect('cadastro.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM pessoas')

    tabela = from_db_cursor(cursor)
    print(tabela)

def pesquisar(cpf=None, nome=None):
    conexao = sqlite3.connect('cadastro.db')

    sql = f"SELECT * FROM pessoas WHERE cpf LIKE '%{cpf}%'"

    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()

    conexao.close()

    return resultado
