from kivy.uix.screenmanager import Screen

#from model.Cliente import Cliente

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine


class FuncionarioScreen(Screen):

    def imprime(self):
        return print(self.ids.iptNomeFuncionario.text)

    def save(self):
        nome = self.ids.iptNomeFuncionario.text
        sobrenome = self.ids.iptSobrenomeFuncionario.text
        cargo = self.ids.iptCargo.text
        return print(nome, sobrenome, cargo)

    pass
