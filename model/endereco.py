class Endereco:
    def __init__(self):
        self._id = 0
        self._estado = ""
        self._cidade = ""
        self._bairro = ""
        self._cep = ""
        self._endereco = ""
        self._n = ""

    # Getter do id
    @property
    def id(self):
        return self._id

    # Getter e Setter do estado
    @property
    def estado(self):
        return self._estado
    @estado.setter
    def estado(self, val):
        self._estado = val

    # Getter e Setter do cidade
    @property
    def cidade(self):
        return self._cidade
    @cidade.setter
    def cidade(self, val):
        self._cidade = val

    # Getter e Setter do bairro
    @property
    def bairro(self):
        return self._bairro
    @bairro.setter
    def bairro(self, val):
        self._bairro = val

    # Getter e Setter do cep
    @property
    def cep(self):
        return self._cep
    @cep.setter
    def cep(self, val):
        self._cep = val

    # Getter e Setter do endereco
    @property
    def endereco(self):
        return self._endereco
    @endereco.setter
    def endereco(self, val):
        self._endereco = val

    #   Getter e Setter do n
    @property
    def n(self):
        return self._n
    @n.setter
    def n(self, val):
        self._n = val