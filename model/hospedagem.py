import cliente
import servicos
import produto
import quarto

class Hospedagem(cliente.Cliente,servicos.Servicos, produto.Produto, quarto.Quarto):
    def __init__(self):
        self._id = 0
        self._checkIn = ""
        self._checkOut = ""
        #idCliente
        #idQuarto
        #idServicos
        #idProduto
        self._valorDiaria = 0
        self._diarias = 0
        self._valorServico = 0
        self._produtos = ""
        self._valorProdutos = 0
        self._desconto = 0
        self._valorTotal = 0

    # Getter do id
    @property
    def id(self):
        return self._id

    # Getter e Setter do checkIn
    @property
    def checkIn(self):
        return self._checkIn
    @checkIn.setter
    def checkIn(self, val):
        self._checkIn = val

    # Getter e Setter do checkOut
    @property
    def checkOut(self):
        return self._checkOut
    @checkOut.setter
    def checkOut(self, val):
        self._checkOut = val

    # Getter e Setter do valorDiaria
    @property
    def valorDiaria(self):
        return self._valorDiaria
    @valorDiaria.setter
    def valorDiaria(self, val):
        self._valorDiaria = val

    # Getter e Setter do diarias
    @property
    def diarias(self):
        return self._diarias
    @diarias.setter
    def diarias(self, val):
        self._diarias = val

    # Getter e Setter do valorServico
    @property
    def valorServico(self):
        return self._valorServico
    @valorServico.setter
    def valorServico(self, val):
        self._valorServico = val

    # Getter e Setter do produtos
    @property
    def produtos(self):
        return self._produtos
    @produtos.setter
    def produtos(self, val):
        self._produtos = val

    # Getter e Setter do valorProdutos
    @property
    def valorProdutos(self):
        return self._valorProdutos
    @valorProdutos.setter
    def valorProdutos(self, val):
        self._valorProdutos = val

    #Getter e Setter do desconto
    @property
    def desconto(self):
        return self._desconto
    @desconto.setter
    def desconto(self, val):
        self._desconto = val

    # Getter e Setter do valorTotal
    @property
    def valorTotal(self):
        return self._valorTotal
    @valorTotal.setter
    def valorTotal(self, val):
        self._valorTotal = val





