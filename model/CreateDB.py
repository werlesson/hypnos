from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, mapper
from sqlalchemy.orm import backref

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database

from datetime import datetime

from model.Cliente import Cliente

_url = 'sqlite:///../database/database.db'

# cria o engine e o declarative_base
engine = create_engine(_url, echo=True)

Base = declarative_base(bind=engine)


class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    teste = Column(String(100), nullable=True)
    id_pessoa = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship("Pessoa", back_populates="clientes")

    __mapper_args__ = {
        'version_id_col': teste,
        'version_id_generator': lambda v: datetime.now()
    }


class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=True)
    sobrenome = Column(String(100), nullable=True)
    id_endereco = Column(Integer, ForeignKey('enderecos.id'))
    endereco = relationship("Endereco", back_populates="pessoas")
    cliente = relationship("Cliente", back_populates="pessoas", uselist=False)


class Endereco(Base):
    __tablename__ = 'enderecos'
    id = Column(Integer, primary_key=True)
    pessoa = relationship("Pessoa", back_populates="enderecos", uselist=False)


if __name__ == '__main__':
    if database_exists(engine.url):
        Base.metadata.drop_all()
    # cria as tabelas no banco (caso nao existam)
    Base.metadata.create_all()


    # configure Session class with desired options
    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()