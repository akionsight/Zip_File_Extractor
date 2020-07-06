import PySimpleGUI as sg
from zip_file_extractor import *
layout = [ [sg.Text("please provide the .zip file")],
            [sg.Input(key='file_path'), sg.FileBrowse(button_text="browse .zip file")],
            [sg.OK(), sg.Cancel()]]

window = sg.Window(title="Zip File Extracter", layout=layout)

while True:
    event, values = window.read()
    if event in ('OK'):
        extract_file(values['file_path'])
        sg.popup('file extracted ✅')
        break
    if event in (None, 'Cancel'):
        break