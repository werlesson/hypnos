import endereco

class Agenda(endereco.Endereco):
    def __init__(self):
        self._id = 0
        self._nomeDoContato = ""
        self._telefone = ""
        #idEndereco


    # Getter do id
    @property
    def id(self):
        return self._id

    # Getter e Setter do nomeDoContato
    @property
    def nomeDoContato(self):
        return self._nomeDoContato
    @nomeDoContato.setter
    def nomeDoContato(self, val):
        self._nomeDoContato = val

    # Getter e Setter do telefone
    @property
    def telefone(self):
        return self._telefone
    @telefone.setter
    def telefone(self, val):
        self._telefone = val