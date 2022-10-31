from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import declarative_base
from main import db

class Item(db.Model):
    id_item = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)