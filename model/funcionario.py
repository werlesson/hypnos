import pessoa1

class Funcionario(pessoa1.Pessoa):
    def __init__(self):
        # idPessoa
        self._id = 0
        self._cargo = ""

    #Getter do id
    @property
    def id(self):
        return self._id

    # Getter e Setter do cargo
    @property
    def cargo(self):
        return self._cargo
    @cargo.setter
    def cargo(self, val):
        self._cargo = val