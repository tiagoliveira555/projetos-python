from funcoes import *
from banco import *

while True:
    limpaTela()
    resposta = menu([
    'CADASTRAR CLIENTES',
    'PESQUISAR CLIENTES',
    'RELATÓRIO',
    'EDITAR CLIENTES',
    'EXCLUIR'
    ])

    if resposta == 0:
        break

    elif resposta == 1:
        limpaTela()
        cabecalho('CADASTRO DE CLIENTES')

        nome = str(input('Nome: '))
        endereco = str(input('Endereço: '))
        cpf = str(input('CPF: '))

        cadastrar_clientes(nome, endereco, cpf)

    elif resposta == 2:
        limpaTela()
        cabecalho('PESQUISA')

        cpf = input('CPF: ')
        pesquisar_clinte(cpf)

    elif resposta == 3:
        cabecalho('RELATÓRIO')

    elif resposta == 4:
        cabecalho('EDITAR')

    elif resposta == 5:
        cabecalho('EXCLUIR')

    else:
        limpaTela()
        print('Opção Inválida!')
        input('[ENTER] para continuar...')
