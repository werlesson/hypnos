class Servicos:
    def __init__(self):
        self._id = 0
        self._nome = ""
        self._categoria = ""
        self._valor = 0
        self._serPorPessoa = 0
        self._serPorDia = 0
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

    # Getter e Setter do serPorPessoa
    @property
    def serPorPessoa(self):
        return self._serPorPessoa
    @serPorPessoa.setter
    def serPorPessoa(self, val):
        self._serPorPessoa = val

    # Getter e Setter do serPorDia
    @property
    def serPorDia(self):
        return self._serPorDia
    @serPorDia.setter
    def serPorDia(self, val):
        self._serPorDia = val

    # Getter e Setter do descricao
    @property
    def descricao(self):
        return self._descricao
    @descricao.setter
    def descricao(self, val):
        self._descricao = val

