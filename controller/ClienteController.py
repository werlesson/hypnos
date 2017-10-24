from kivy.uix.screenmanager import Screen
from model.CreateDB import Cliente, engine

#from model.Cliente import Cliente

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine


def connectToDatabase():
    """
    Connect to our SQLite database and return a Session object
    """
    engine = create_engine("sqlite:///../database/database.db", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


class ClienteScreen(Screen):

    def insert_cliente(self):
        session = connectToDatabase()
        session.add(self.ids.iptNomeCliente.text)
        session.commit()
        session.close()

#        print("Teste")
#        conn = engine.connect()
# ins = Cliente.__tablename__.insert()
#  new_cliente = ins.values(self.iptNomeCliente.text)
#  conn.execute(new_cliente)

    def imprime(self):
        return print(self.ids.iptNomeCliente.text)

    def save(self):
        nome = self.ids.iptNomeCliente.text
        sobrenome = self.ids.iptSobrenomeCliente.text
        return print(nome, sobrenome)

    pass
