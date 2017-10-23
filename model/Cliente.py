from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, mapper

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database

_url = 'sqlite:///../database/database.db'

# cria o engine e o declarative_base
engine = create_engine(_url, echo=True)

Base = declarative_base(bind=engine)


class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    sobrenome = Column(String(100), nullable=True)

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def __repr__(self):
        return '<Cliente {0}>'.format(self.nome, self.sobrenome)

if __name__ == '__main__':
    if database_exists(engine.url):
        Base.metadata.drop_all()
    # cria as tabelas no banco (caso nao existam)
    Base.metadata.create_all()

    # configure Session class with desired options
    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()


def save(nome, sobrenome):
    cliente = Cliente(nome, sobrenome)
    session.add(cliente)
    session.commit()
