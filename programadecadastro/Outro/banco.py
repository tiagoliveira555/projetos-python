import sqlite3
from prettytable import from_db_cursor

def criar_banco():
    conexao = sqlite3.connect('programa.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                endereco TEXT NOT NULL,
                cpf TEXT NOT NULL)''')
    
    cursor.close()
    conexao.close()


def cadastrar_clientes(nome, endereco, cpf):
    conexao = sqlite3.connect('programa.db')

    val = (nome, endereco, cpf)
    sql = 'INSERT INTO clientes(nome, endereco, cpf) VALUES (?, ?, ?)'

    cursor = conexao.cursor()
    cursor.execute(sql, val)
    conexao.commit()

    cursor.close()
    conexao.close()


'''def relatorio_clientes():
    conexao = sqlite3.connect('programa.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM clientes')

    lista = cursor.fetchall()
    tabela = PrettyTable(['ID', 'NOME', 'ENDERECO', 'CPF'])

    for l in lista:
        id = [l[0]]
        nome = [l[1]]
        endereco = [l[2]]
        cpf = [l[3]]
        for p in range(len(id)):
            tabela.add_row([id[p], nome[p], endereco[p], cpf[p]])
        
    print(tabela)

    cursor.close()
    conexao.close()
'''

def relatorio_clientes():
    conexao = sqlite3.connect('Outro/programa.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM clientes')
    tabela = from_db_cursor(cursor)

    print(tabela)

