from funcoes import *
from bd import *


while True:
    resposta = menu([
        'ADICIONAR CLIENTE',
        'RELATÓRIO DE CLIENTES',
        'PESQUISAR CLIENTE',
        'EDITAR CLIENTE',
        'EXCLUIR CLIENTE'])

    if resposta == 0:
        sair = str(input('\033[33mDeseja realmente sair? [S/N]:\033[m ')).upper()
        while sair not in 'SN' or sair == '':
            print('Digite S ou N')
            sair = str(input('\033[33mDeseja realmente sair? [S/N]:\033[m ')).upper()
            
        if sair == 'S':
            break

    elif resposta == 1:
        limpar_tela()
        while True:
            cabecalho('ADICIONANDO CLIENTE')
            nome = str(input('\033[32mNome:\033[m '))
            endereço = str(input('\033[32mEndereço:\033[m '))
            cpf = str(input('\033[32mCPF:\033[m '))
            cadastrar(nome, endereço, cpf)

            sair = ''
            while sair not in 'SN' or sair == '':
                sair = str(input('\033[33mQuer cadastrar outro cliente? [S/N]:\033[m ')).upper()
                print('Digite S ou N')

            limpar_tela()
            if sair in 'N':
                break

    elif resposta == 2:
        limpar_tela()
        cabecalho('RELATÓRIO')
        relatorio()
        print()
        input('[ENTER] para continuar...')

    elif resposta == 3:
        limpar_tela()
        cabecalho('PESQUISANDO CLIENTE')
        cpf = input('CPF: ')
        linha()
        c = pesquisar(cpf)

        for i in c:
            print(f'\033[32mNome    :\033[m {i[1]}')
            print(f'\033[32mEndereço:\033[m {i[2]}')
            print(f'\033[32mCPF     :\033[m {i[3]}')
            linha()

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
