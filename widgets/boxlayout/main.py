#coding: utf-8

import kivy
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.1')
from kivy.app import App

code = """ 
BoxLayout:
    orientation: "vertical"
    Button:
        background_color: 0, .2, .7, 1
        text: "A"
        size_hint: 1., 1.
    Image:
        source: '1073.png'
        size_hint: 1., 1.        
    Button:
        background_color: 0, .2, .7, 1
        text: "C"
        size_hint: 1., 1.    
"""

from kivy.lang import Builder

class BoxlayoutApp(App):
    def build(self):
        return Builder.load_string(code)

from kivy.core.window import Window
Window.clearcolor = [1,1,1,1]

janela = BoxlayoutApp()
janela.run()