from kivy.uix.screenmanager import Screen

#from model.Cliente import Cliente

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine


class EnderecoScreen(Screen):

    def imprime(self):
        return print(self.ids.iptCidadeEndereco.text)

    def save(self):
        estado = self.ids.iptEstadoEndereco.text
        cidade = self.ids.iptCidadeEndereco.text
        bairro = self.ids.iptBairroEndereco.text
        cep = self.ids.iptCepEndereco.text
        endereco = self.ids.iptEnderecoEndereco.text
        numero = self.ids.iptNumeroEndereco.text
        return print(estado, cidade, bairro, cep, endereco, numero)

    pass
