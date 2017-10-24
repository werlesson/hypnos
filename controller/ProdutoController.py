from kivy.uix.screenmanager import Screen

#from model.Cliente import Cliente

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine


class ProdutoScreen(Screen):

    def imprime(self):
        return print(self.ids.iptNomeProduto.text)

    def save(self):
        nome = self.ids.iptNomeProduto.text
        categoria = self.ids.iptCategoriaProduto.text
        valor = self.ids.iptValorProduto.text
        quantidade = self.ids.iptQuantidadeProduto.text
        descricao = self.ids.iptDescricaoProduto.text
        return print(nome, categoria, valor, quantidade, descricao)

    pass
