import pessoa1

class Cliente(pessoa1.Pessoa):
    def __init__(self):
        #idPessoa
        self._id = 0
        self._observacao = ""
        self._tipo = ""
        self._categoria = ""

    # Getter do id
    @property
    def id(self):
        return self._id

    # Getter e Setter do observacao
    @property
    def observacao(self):
        return self._observacao
    @observacao.setter
    def observacao(self, val):
        self._observacao = val

    # Getter e Setter do tipo
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, val):
        self._tipo = val

    # Getter e Setter do categoria
    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, val):
        self._categoria = val