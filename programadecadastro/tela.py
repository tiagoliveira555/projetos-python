import os


def leiaInt(num):
    try:
        n = int(input(num))
    except(ValueError, TypeError):
        print('ERRO! Digite um número válido!')
    else:
        return n


def limpaTela():
    os.system('clear')


def linha():
    print('-' * 30)


def cabecalho(txt):
    linha()
    print(txt.center(30))
    linha()


def menu(msg):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in msg:
        print(f'[ {c} ] - {i}')
        c += 1
    print()
    print('[ 0 ] - SAIR')
    linha()

    res = leiaInt('Qual a opção? ')
    return res
