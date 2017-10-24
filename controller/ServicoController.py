from kivy.uix.screenmanager import Screen

#from model.Cliente import Cliente

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine


class ServicoScreen(Screen):

    def imprime(self):
        return print(self.ids.iptNomeServico.text)

    def save(self):
        nome = self.ids.iptNomeServicos.text
        categoria = self.ids.iptCategoriaServico.text
        valor = self.ids.iptValorServico.text
        servicoPPessoa = self.ids.iptServicoPPessoa.text
        servicoPDia = self.ids.iptServicoPDia.text
        descricao = self.ids.iptDescricaoProduto.text
        return print(nome, categoria, valor, servicoPPessoa, servicoPDia, descricao)

    pass
