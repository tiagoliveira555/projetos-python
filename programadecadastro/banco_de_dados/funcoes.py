import os

Nomes = []
Endereços = []
CPFs = []

def limpar_tela():
    os.system('clear')

def leiaInt(num):
    try:
        n = int(input(num))
    except (TypeError, ValueError):
        print('\033[33mERRO! Digite um número válido!\033[m')
    else:
        return n

def linha():
    print('-' * 30)

def cabecalho(txt):
    linha()
    print(txt.center(30))
    linha()

def menu(msg):
    limpar_tela()
    cabecalho('MENU')
    c = 1
    for m in msg:
        print(f'\033[33m[\033[m {c} \033[33m]\033[m - \033[34m{m}\033[m')
        c += 1
    print()
    print('\033[33m[\033[m 0 \033[33m]\033[m - \033[34mSAIR\033[m')
    linha()
    opc = leiaInt('\033[32mQual sua opção?\033[m ')
    return opc

def adicionar(n, e, c):
    global Nomes, Endereços, CPFs
    Nomes.append(n)
    Endereços.append(e)
    CPFs.append(c)

    print(f'{n} adicionado com sucesso!')

def relatorio():
    global Nomes, Endereços, CPFs
    for n in range(len(Nomes)):
        print(f'Nome    : {Nomes[n]}')
        print(f'Endereço: {Endereços[n]}')
        print(f'CPF     : {CPFs[n]}')
        linha()
    input('[ENTER] para continuar...')

def pesquisar(cpf):
    global CPFs
    if cpf in CPFs:
        return CPFs.index(cpf)
    return -1

def editar(cpf):
    global Nomes, Endereços, CPFs
    c = pesquisar(cpf)

    if c != -1:
        print(f'Nome    : {Nomes[c]}')
        print(f'Endereço: {Endereços[c]}')
        print(f'CPF     : {CPFs[c]}')
        print('____________________________')
        print('Digite um novo valor ou [ENTER] para permanecer o atual')
        novo_n = input('Novo Nome: ')
        novo_e = input('Novo Endereço: ')
        novo_c = input('Novo CPF: ')

        if novo_n != '':
            Nomes[c] = novo_n
        if novo_e != '':
            Endereços[c] = novo_e
        if novo_c != '':
            CPFs[c] = novo_c

    print('Dados alterados com sucesso.')
    input('[ENTER] para continuar...')

def excluir(cpf):
    global Nomes, Endereços, CPFs
    c = pesquisar(cpf)
    if c != -1:
        print(f'Nome    : {Nomes[c]}')
        print(f'Endereço: {Endereços[c]}')
        print(f'CPF     : {CPFs[c]}')
        print('____________________________')

        e = input('Tem certeza que deseja excuir? [S/N] ').upper()
        if e == 'S':
            del Nomes[c]
            del Endereços[c]
            del CPFs[c]
            print('Usuário deletado com sucesso!')
            input('[ENTER] para continuar...' )
        else:
            input('[ENTER] para continuar...')
