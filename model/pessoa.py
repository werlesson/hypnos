from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine

Base = declarative_base()

"""
class User(Base):
    __tablename__ = 'users'

    username = Column(String(20), nullable=False, primary_key=True)
    password = Column(String(20), nullable=False)
"""


class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    sobrenome = Column(String(100), nullable=True)

"""
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def __repr__(self):
        return '<Pessoa {0}>'.format(self.nome, self.sobrenome)
"""


engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
