class Produto:
    def __init__(self):
        self._id = 0
        self._nome = ""
        self._categoria = ""
        self._valor = 0
        self._quantidade = 0
        self._descricao = ""

    # Getter do id
    @property
    def id(self):
        return self._id

    # Getter e Setter do nome
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, val):
        self._nome = val

    # Getter e Setter do categoria
    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, val):
        self._categoria = val

    # Getter e Setter do valor
    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self, val):
        self._valor = val

    # Getter e Setter do quantidade
    @property
    def quantidade(self):
        return self._quantidade
    @quantidade.setter
    def quantidade(self, val):
        self._quantidade = val

    # Getter e Setter do descricao
    @property
    def descricao(self):
        return self._descricao
    @descricao.setter
    def descricao(self, val):
        self._descricao = val