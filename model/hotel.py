import endereco

class Hotel(endereco.Endereco):
    def __init__(self):
        self._id = 0
        self._nomeFantasia = ""
        self._razaoSocial = ""
        self._email = ""
        self._homepage = ""
        self._telefone = ""
        self._cnpj = ""
        self._inscricaoEstadual = ""
        self._inscricaoEmbratur = ""
        #idEndereco

    # Getter do id
    @property
    def id(self):
        return self._id

    # Getter e Setter do nomeFantasia
    @property
    def nomeFantasia(self):
        return self._nomeFantasia
    @nomeFantasia.setter
    def nomeFantasia(self, val):
        self._nomeFantasia = val

    # Getter e Setter do razaoSocial
    @property
    def razaoSocial(self):
        return self._razaoSocial
    @razaoSocial.setter
    def razaoSocial(self, val):
        self._razaoSocial = val

    # Getter e Setter do email
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, val):
        self._email = val

    # Getter e Setter do homepage
    @property
    def homepage(self):
        return self._homepage
    @homepage.setter
    def homepage(self, val):
        self._homepage = val

    # Getter e Setter do telefone
    @property
    def telefone(self):
        return self._telefone
    @telefone.setter
    def telefone(self, val):
        self._telefone = val

    # Getter e Setter do cnpj
    @property
    def cnpj(self):
        return self._cnpj
    @cnpj.setter
    def cnpj(self, val):
        self._cnpj = val

    # Getter e Setter do inscricaoEstadual
    @property
    def inscricaoEstadual(self):
        return self._inscricaoEstadual
    @inscricaoEstadual.setter
    def inscricaoEstadual(self, val):
        self._inscricaoEstadual = val

    # Getter e Setter do inscricaoEmbratur
    @property
    def inscricaoEmbratur(self):
        return self._inscricaoEmbratur
    @inscricaoEmbratur.setter
    def inscricaoEmbratur(self, val):
        self._inscricaoEmbratur = val

