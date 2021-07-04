import mysql.connector


def conecta_banco():
    conexao = mysql.connector.connect(
    host='localhost',
    user='admin',
    passwd='admin',
    db='db_clientes'
    )

    return conexao


def cadastrar_clientes(nome, endereco, cpf):
    conexao = conecta_banco()

    val = (nome, endereco, cpf)
    sql = 'INSERT INTO clientes(nome, endereco, cpf) VALUE (%s, %s, %s)'

    cursor = conexao.cursor()
    cursor.execute(sql, val)
    conexao.commit()

    cursor.close()
    conexao.close()


def pesquisar_clinte(cpf=None):
    conexao = conecta_banco()

    sql = f"SELECT * FROM clientes WHERE cpf LIKE '%{cpf}%'"

    cursor = conexao.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado
