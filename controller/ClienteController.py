from kivy.uix.screenmanager import Screen

#from model.Cliente import Cliente

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine


class ClienteScreen(Screen):

    def imprime(self):
        return print(self.ids.iptNomeCliente.text)

    def save(self):
        nome = self.ids.iptNomeCliente.text
        sobrenome = self.ids.iptSobrenomeCliente.text
        return print(nome, sobrenome)

    pass
