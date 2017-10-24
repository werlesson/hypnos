from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    sobrenome = Column(String(100), nullable=True)
    teste = Column(String(100), nullable=True)

    def __init__(self, nome, sobrenome, teste):
        self.nome = nome
        self.sobrenome = sobrenome
        self.teste = teste

    def __repr__(self):
        return '<Cliente {0}>'.format(self.nome, self.sobrenome, self.teste)
