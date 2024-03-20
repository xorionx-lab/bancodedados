from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///projeto.db"

engine = create_engine(CONN, echo = True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Cliente(Base):
    __tablename__ = "Cliente"
    id = Column(Integer, primary_key=True)
    titulo = Column(String())
    valor = Column(Float())

Base.metadata.create_all(engine)