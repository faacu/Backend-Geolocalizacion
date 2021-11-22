from db import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

class PaisBd(Base):
    __tablename__ = 'Paises'

    id = Column(Integer, primary_key=True)
    pa_nombre = Column(String(80), nullable=False)
    cantidadHabitantes = Column(Integer, nullable=False)

class PaisSinId(BaseModel):
    pa_nombre: str
    cantidadHabitantes : int

    class Config:
        orm_mode = True

class PaisApi(PaisSinId):
    id: int
