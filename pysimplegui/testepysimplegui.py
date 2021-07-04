import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Nome', size=(5, 0)), sg.Input(size=(15, 0), key='nome')],
            [sg.Text('Idade', size=(5, 0)), sg.Input(size=(15, 0), key='idade')],
            [sg.Text('Quais provedores de email são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook',
                key='outlook')],
            [sg.Text('Aceita cartão?')],
            [sg.Radio('Sim', 'cartões', key='aceitaCartão'),
                sg.Radio('Não', 'cartões', key='naoAceitaCartão')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30, 10))]
        ]

        self.janela = sg.Window('Dados do Usuário').layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            gmail = self.values['gmail']
            outlook = self.values['outlook']
            aceita_cartão = self.values['aceitaCartão']
            nao_aceita_cartão = self.values['naoAceitaCartão']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Gmail: {gmail}')
            print(f'Outlook: {outlook}')
            print(f'Aceita Cartão: {aceita_cartão}')
            print(f'Não aceita cartão: {nao_aceita_cartão}')


tela = TelaPython()
tela.Iniciar()
