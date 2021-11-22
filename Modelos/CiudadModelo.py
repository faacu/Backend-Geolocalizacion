from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from pydantic import BaseModel
from sqlalchemy.orm import relationship

class CiudadBd(Base):
    __tablename__ = 'Ciudades'

    id = Column(Integer, primary_key=True)
    ci_nombre = Column(String(80), nullable=False)
    descripcion = Column(String(500))
    provincias = relationship('Modelos.ProvinciaModelo.ProvinciaBd', lazy='joined')
    id_provincia = Column(Integer, ForeignKey('Provincias.id'))

class CiudadSinId(BaseModel):
    ci_nombre: str
    descripcion : str
    id_provincia: int

    class Config:
        orm_mode = True

class CiudadApi(CiudadSinId):
    id: int
