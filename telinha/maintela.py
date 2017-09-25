#coding: utf-8

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

def build():
    global ed  # isso aqui não é boa pratica
    layout = FloatLayout()
    ed = TextInput(text = "eXcript")

    ed.size_hint = None, None
    ed.height = 300
    ed.width = 400
    ed.x = 60
    ed.y = 250

    bt = Button(text = "Clique aqui")
    bt.size_hint = None, None
    bt.height = 50
    bt.width = 200
    bt.y = 150
    bt.x = 170
    bt.on_press = click

    layout.add_widget(ed)
    layout.add_widget(bt)
    return layout

def click():
    print(ed.text)

janela = App()
janela.title = "eXcript"

from kivy.core.window import Window
Window.size = 600,600

janela.build = build
janela.run()