import funcionario

class Usuario(funcionario.Funcionario):
    def __init__(self):
        # idFuncionario
        self._id = 0
        self._usuario = ""
        self._senha = ""
        self._tipoDeUsuario = ""

    #Getter do id
    @property
    def id(self):
        return self._id

    # Getter e Setter do usuario
    @property
    def usuario(self):
        return self._usuario
    @usuario.setter
    def usuario(self, val):
        self._usuario = val

    # Getter e Setter do senha
    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, val):
        self._senha = val

    # Getter e Setter do tipoDeUsuario
    @property
    def tipoDeUsuario(self):
        return self._tipoDeUsuario
    @tipoDeUsuario.setter
    def tipoDeUsuario(self, val):
        self._tipoDeUsuario = val