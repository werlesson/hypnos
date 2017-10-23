
# coding: utf-8

# exemplos de relacionamentos em http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker, mapper

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database, drop_database

_url = 'sqlite:///database.db'

# cria o engine e o declarative_base
engine = create_engine(_url, echo=True)

Base = declarative_base(bind=engine)


# Relacionamento Um para Muitos
# Endereco - pessoas

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    
    enderecos = relationship("Endereco", backref="pessoa")

    def __init__(self, nome):
        self.nome = nome
        
    def __repr__(self):
        return '<Pessoa {0}>'.format(self.nome)


class Endereco(Base):
    __tablename__ = 'enderecos'
    id = Column(Integer, primary_key=True)
    logradouro = Column(String(100), nullable=False)
    id_pessoa = Column(Integer, ForeignKey('pessoas.id'), nullable=False)

    def __init__(self, logradouro, id_pessoa):
        self.logradouro = logradouro
        self.id_pessoa = id_pessoa
        
    def __repr__(self):
        return '<Endereco {0}'.format(self.logradouro)

# Many to Many
'''class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(20), nullable=False)
    
class Tags(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(20), nullable=False)'''    


if __name__ == '__main__':
    if database_exists(engine.url):
        Base.metadata.drop_all()
    #cria as tabelas no banco (caso nao existam)
    Base.metadata.create_all()
    
    
    # configure Session class with desired options
    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()
 
    pessoa = Pessoa('Cicrano')
    session.add(pessoa)
    session.commit()

    e = Endereco('Rua do Fulano', pessoa.id)
    session.add(e)
    session.commit()
    
    print(pessoa.enderecos)
    print(e.pessoa)