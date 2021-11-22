from db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from pydantic import BaseModel

class ProvinciaBd(Base):
    __tablename__ = 'Provincias'

    id = Column(Integer, primary_key=True)
    pr_nombre = Column(String(80), nullable=False)
    descripcion = Column(String(500))
    paises = relationship('Modelos.PaisModelo.PaisBd', lazy='joined')
    id_pais = Column(Integer, ForeignKey('Paises.id'))

class ProvinciaSinId(BaseModel):
    pr_nombre: str
    descripcion : str
    id_pais: int

    class Config:
        orm_mode = True


class ProvinciaApi(ProvinciaSinId):
    id: int
