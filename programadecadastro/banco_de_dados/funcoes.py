import os


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
