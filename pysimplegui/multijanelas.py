import PySimpleGUI as sg


def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layout, finalize=True)


def janela_pedidos():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Hamburger', key='hamburger'), sg.Checkbox('Refrigerante', key='refrigerante')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]
        ]
    return sg.Window('Montar Pedido', layout=layout, finalize=True)


janela1, janela2 = janela_login(), None

while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WINDOW_CLOSED or window == janela2 and event == sg.WINDOW_CLOSED:
        break
    elif window == janela1 and event == 'Continuar':
        janela2 = janela_pedidos()
        janela1.hide()
    elif window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    elif window == janela2 and event == 'Fazer Pedido':
        if values['hamburger'] == True and values['refrigerante'] == True:
            sg.popup('Foram solicitados um Hamburger e um refrigerante')
        elif values['hamburger'] == True:
            sg.popup('Foi solicitado um Hamburger')
        elif values['refrigerante'] == True:
            sg.popup('Foi solicitado um refrigerante')
