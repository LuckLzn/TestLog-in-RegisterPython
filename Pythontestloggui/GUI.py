from PySimpleGUI import PySimpleGUI as sg

class Window1:
    #Layout
    sg.theme('Reddit')
    layout = [
        [sg.Text("Usuario"),sg.Input(key = 'usuario', size=(25,1))],
        [sg.Text("Senha"),sg.Input(key = 'senha', password_char = '*', size=(25,1))],
        [sg.Checkbox('Salvar o login?')],
        [sg.Button('Entrar')]
    ]
    #Window
    window = sg.Window('Tela de Login', layout)
    #Read Events
    while True:
        eventos, valores = window.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Entrar':
            if valores['usuario'] == 'Lucas' and valores['senha'] == '1234':
                print("Welcome", valores['usuario'])
                break