from tela import *
from banco import *


def cadastrar():
 
    limpaTela()
    cabecalho('CADASTRO DE CLIENTES')

    nome = str(input('Nome: '))
    endereco = str(input('Endereço: '))
    cpf = str(input('CPF: '))

    cadastrar_clientes(nome, endereco, cpf)
