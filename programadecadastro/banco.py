import sqlite3


def conecta_banco():
    conexao = sqlite3.connect('programa.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                endereco TEXT NOT NULL,
                cpf TEXT NOT NULL)''')

    return conexao


def cadastrar_clientes(nome, endereco, cpf):
    conexao = conecta_banco()

    val = (nome, endereco, cpf)
    sql = 'INSERT INTO clientes(nome, endereco, cpf) VALUES (?, ?, ?)'

    cursor = conexao.cursor()
    cursor.execute(sql, val)
    conexao.commit()

    cursor.close()
    conexao.close()


def pesquisar_clinte(cpf=None):
    conexao = conecta_banco()

    sql = "SELECT * FROM clientes WHERE cpf LIKE 'cpf'"

    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado
