from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.pessoa import Pessoa

engine = create_engine('sqlite:///database.db')
DBSession = sessionmaker()
DBSession.configure(bind=engine)
session = DBSession()

new_user = Pessoa(nome='python', sobrenome='is_fun')
session.add(new_user)
session.commit()