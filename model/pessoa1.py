import endereco

class Pessoa(endereco.Endereco):
    def __init__(self):
        self._id = 0
        self._nome = ""
        self._cpf = ""
        self._dataNasc = ""
        self._nacionalidade = ""
        self._profissao = ""
        self._passaporte = ""
        self._pais = ""
        self._email = ""
        self._telefone = ""
        ##id endereço

    #Getter do id
    @property
    def id(self):
        return  self._id

    #Getter e Setter do nome
    @property
    def nome(self):
        return  self._nome
    @nome.setter
    def nome(self, val):
        self._nome = val

    # Getter e Setter do cpf
    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, val):
        self._cpf = val

    # Getter e Setter do dataNasc
    @property
    def dataNasc(self):
        return self._dataNasc
    @dataNasc.setter
    def dataNasc(self, val):
        self._dataNasc = val

    # Getter e Setter do nacionalidade
    @property
    def nacionalidade(self):
        return self._nacionalidade
    @nacionalidade.setter
    def nacionalidade(self, val):
        self._nacionalidade= val

    # Getter e Setter do profissao
    @property
    def profissao(self):
        return self._profissao
    @profissao.setter
    def profissao(self, val):
        self._profissao = val

    # Getter e Setter do passaporte
    @property
    def passaporte(self):
        return self._passaporte
    @passaporte.setter
    def passaporte(self, val):
        self._passaporte = val

    # Getter e Setter do pais
    @property
    def pais(self):
        return self._pais
    @pais.setter
    def pais(self, val):
        self._pais = val

    # Getter e Setter do email
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, val):
        self._email = val

    # Getter e Setter do telefone
    @property
    def telefone(self):
        return self._telefone
    @telefone.setter
    def telefone(self, val):
        self._telefone = val

