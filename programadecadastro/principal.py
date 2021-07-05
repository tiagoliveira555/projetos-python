from gerente import *
from tela import *


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
        cadastrar()

    elif resposta == 2:
        cabecalho('PESQUISAR')

    elif resposta == 3:
        relatorio()

    elif resposta == 4:
        cabecalho('EDITAR')

    elif resposta == 5:
        cabecalho('EXCLUIR')

    else:
        limpaTela()
        print('Opção Inválida!')
        input('[ENTER] para continuar...')
