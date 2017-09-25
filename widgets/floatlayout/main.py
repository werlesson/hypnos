#coding: utf-8

import kivy
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.1')
from kivy.app import App

code = """ 
FloatLayout:
    Button:
        text: "B"
        size_hint: .2, .2
        pos_hint: {"center_x":.5, "center_y":.5}
    Button:
        text: "A"
        size_hint: .1, .1
        pos_hint: {"x":0, "top": 1.}
    Button:
        text: "C"
        size_hint: .1, .1
        pos_hint: {"y": 0, "right": 1.}
    Button:
        text: "Absoluto"
        size_hint: None, None
        pos_hint: {"center_y": .7}
        x: 150
        width: 200
        heigth: 100
"""

from kivy.lang import Builder

class FloatlayoutApp(App):
    def build(self):
        return Builder.load_string(code)

janela = FloatlayoutApp()
janela.run()