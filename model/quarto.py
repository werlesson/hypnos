import agenda

class Quarto(agenda.Agenda):
    def __init__(self):
        self._id = 0
        self._numero = 0
        self._descricao = ""
        self._tipoDeQuarto = ""
        self._status = ""
        self._dataDaUltimaLimpeza = ""
        self._situacaoLimpeza = ""
        self._ramal = ""
        self._qtdCamasDeCasal = ""
        self._qtdCamasDeSolteiro = ""
        self._maximoDeHospedes = 0
        self._minimoDeHospedes = 0
        # idAgenda


    # Getter do id
    @property
    def id(self):
        return self._id

    # Getter e Setter do numero
    @property
    def numero(self):
        return self._numero
    @numero.setter
    def numero(self, val):
        self._numero = val

    # Getter e Setter do descricao
    @property
    def descricao(self):
        return self._descricao
    @descricao.setter
    def descricao(self, val):
        self._descricao = val

    # Getter e Setter do tipoDeQuarto
    @property
    def tipoDeQuarto(self):
        return self._tipoDeQuarto
    @tipoDeQuarto.setter
    def tipoDeQuarto(self, val):
        self._tipoDeQuarto = val

    # Getter e Setter do status
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, val):
        self._status = val

    # Getter e Setter do dataDaUltimaLimpeza
    @property
    def dataDaUltimaLimpeza(self):
        return self._dataDaUltimaLimpeza
    @dataDaUltimaLimpeza.setter
    def dataDaUltimaLimpeza(self, val):
        self._dataDaUltimaLimpeza = val

    # Getter e Setter do situacaoLimpeza
    @property
    def situacaoLimpeza(self):
        return self._situacaoLimpeza
    @situacaoLimpeza.setter
    def situacaoLimpeza(self, val):
        self._situacaoLimpeza = val

    # Getter e Setter do ramal
    @property
    def ramal(self):
        return self._ramal
    @ramal.setter
    def ramal(self, val):
        self._ramal = val

    # Getter e Setter do qtdCamasDeCasal
    @property
    def qtdCamasDeCasal(self):
        return self._qtdCamasDeCasal
    @qtdCamasDeCasal.setter
    def qtdCamasDeCasal(self, val):
        self._qtdCamasDeCasal = val

    # Getter e Setter do qtdCamasDeSolteiro
    @property
    def qtdCamasDeSolteiro(self):
        return self._qtdCamasDeSolteiro
    @qtdCamasDeSolteiro.setter
    def qtdCamasDeSolteiro(self, val):
        self._qtdCamasDeSolteiro = val

    # Getter e Setter do maximoDeHospedes
    @property
    def maximoDeHospedes(self):
        return self._maximoDeHospedes
    @maximoDeHospedes.setter
    def maximoDeHospedes(self, val):
        self._maximoDeHospedes = val

    # Getter e Setter do minimoDeHospedes
    @property
    def minimoDeHospedes(self):
        return self._minimoDeHospedes
    @minimoDeHospedes.setter
    def minimoDeHospedes(self, val):
        self._minimoDeHospedes = val

