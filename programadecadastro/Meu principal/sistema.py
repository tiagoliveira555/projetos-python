from time import sleep
from funcoes import *

while True:
    resposta = menu([
        'ADICIONAR CLIENTE',
        'RELATÓRIO DE CLIENTES',
        'PESQUISAR CLIENTE',
        'EDITAR CLIENTE',
        'EXCLUIR CLIENTE'])

    if resposta == 0:
        break

    elif resposta == 1:
        limpar_tela()
        while True:
            cabecalho('ADICIONANDO CLIENTE')
            nome = str(input('Nome: '))
            endereço = str(input('Endereço: '))
            cpf = str(input('CPF: '))
            adicionar(nome, endereço, cpf)

            sair = ''
            while sair not in 'SN' or sair == '':
                sair = str(input('Quer cadastrar outro cliente? [S/N]: ')).upper()
                print('Digite S ou N')
            limpar_tela()
            if sair in 'N':
                break
    elif resposta == 2:
        limpar_tela()
        cabecalho('RELATÓRIO')
        relatorio()

    elif resposta == 3:
        limpar_tela()
        cabecalho('PESQUISANDO CLIENTE')
        cpf = input('CPF: ')
        c = pesquisar(cpf)
        if c != -1:
            print(f'Nome: {Nomes[c]}')
            print(f'Endereço: {Endereços[c]}')
            print(f'CPF: {CPFs[c]}')
        else:
            print('CPF não encontrado!')

        input('[ENTER] para continuar...')

    elif resposta == 4:
        limpar_tela()
        cabecalho('EDITANDO CLIENTE')
        cpf = str(input('CPF: '))
        editar(cpf)

    elif resposta == 5:
        limpar_tela()
        cabecalho('EXCUINDO CLIENTE')
        cpf = str(input('CPF: '))
        excluir(cpf)

    else:
        print('\033[31mERRO! Opção inválida!\033[m')
        input('[ENTER] para continuar...')
cabecalho('Fim do sistema. Volte sempre!')
