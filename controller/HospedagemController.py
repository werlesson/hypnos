from kivy.uix.screenmanager import Screen

#from model.Cliente import Cliente

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine


class HospedagemScreen(Screen):

    def imprime(self):
        return print(self.ids.iptCheckInHospedagem.text)

    def save(self):
        checkIn = self.ids.iptCheckInHospedagem.text
        checkOut = self.ids.iptCheckOutHospedagem.text
        valorDaDiaria = self.ids.iptValorDaDiariaHospedagem.text
        diarias = self.ids.iptDiariasHospedagem.text
        valorServico = self.ids.iptValorServicoHospedagem.text
        produtos = self.ids.iptProdutosHospedagem.text
        valorProdutos = self.ids.iptValorProdutosHospedagem.text
        desconto = self.ids.iptDescontoHospedagem.text
        valorTotal = self.ids.iptValorTotalHospedagem.text
        return print(checkIn, checkOut, valorDaDiaria,
                     diarias, valorServico, produtos,
                     valorProdutos, desconto, valorTotal)

    pass
