import PySimpleGUI as sg
from project import encode, detect

sg.theme('black')

layout1 = [
    [sg.Text("        WELCOME TO OUR",font='Georgia 20 bold')],
    [sg.Text("                  PROJECT!", font='Georgia 20 bold')],
    [sg.Text("")],
    [sg.Text("ENCODE",font='Georgia 15 bold')],
    [sg.Multiline(key="-IN-", size=(50, 5))],
    [sg.Text("KEY",font='Georgia 15 bold')],
    [sg.Input(size=(44,5), key="-KEY-", enable_events=True), sg.Button('clear', visible=True)],
    ]
layout2 = [
    [sg.Text("")],
    [sg.Text("")],
    [sg.Text("")],
    [sg.Text("ENCODED TEXT",font='Georgia 15 bold')],
    [sg.Multiline('', size=(50,10), key='-OUT-')]
    ]
layout = [
    [sg.Column(layout1, key='-LAYOUT1-'), sg.Column(layout2, visible=False, key='-LAYOUT2-')],
    [sg.Text("")],
    [sg.Text("", key="-ERROR-", font=('Georgia 10 bold'), text_color='#A60000', visible=True)],
    [sg.Button("let's go", visible=True, font=20, border_width=5),sg.Button("back", visible=False, font=20, border_width=5), sg.Button('exit', visible=True, font=20, border_width=5)]
    ]
# create the window

window = sg.Window('Encoder', layout, size=[500,500],element_justification='center')

layout = 1 # The currently visible layout
while True:
    event, values = window.read()
    
    if event == "exit" or event == sg.WIN_CLOSED:
        break
    
    if event == '-KEY-' and values['-KEY-'] and values['-KEY-'][-1] not in ('0123456789.-'):
        window['-KEY-'].update(values['-KEY-'][:-1])
        window["-ERROR-"].update("KEY MUST CONTAIN ONLY NUMBERS!")
    
    message = values["-IN-"]
    shifr = values["-KEY-"]

    if event == "clear":
        window["-KEY-"].update("")
        window["-IN-"].update("")
        window["-OUT-"].update("")
        
    elif event == "let's go":
        if values["-IN-"] and values["-KEY-"]:
            key = int(shifr)
            result = encode(message, key)
            window["-OUT-"].update(result)
            
            window[f'-LAYOUT{layout}-'].update(visible=False)
            layout += 1
            window[f'-LAYOUT{layout}-'].update(visible=True)
            window["-OUT-"].update(result)
            window["let's go"].update(visible=False)
            window['back'].update(visible=True)
            window['clear'].update(visible=False)
            window['-ERROR-'].update(visible=False)
        else:
            window["-ERROR-"].update("ENTER A TEXT ON KEY!")
            
    elif event == "back":
        window[f'-LAYOUT{layout}-'].update(visible=False)
        layout -= 1
        window[f'-LAYOUT{layout}-'].update(visible=True)
        window['back'].update(visible=False)
        window["let's go"].update(visible=True)
        window['clear'].update(visible=True)
        
    
        
window.close()


