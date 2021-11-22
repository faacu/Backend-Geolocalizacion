from fastapi import APIRouter, Depends
from db import get_session
from sqlalchemy.orm import Session
from Repositorios.ProvinciasRepositorio import Provinciarepo
from Modelos.ProvinciaModelo import ProvinciaSinId, ProvinciaApi
from typing import List
from fastapi.exceptions import HTTPException


provincias_router = APIRouter(prefix='/provincias', tags=['Provincias'])
repositorio = Provinciarepo()

@provincias_router.get('/')
def get_all(s: Session = Depends(get_session)):
    """Devuelve una lista con todas las provincias"""
    return repositorio.get_all_provincias(s)

@provincias_router.get('/sin_id', response_model=List[ProvinciaSinId])
def get_provincia_sin_id(s: Session = Depends(get_session)):
    """Devuelve una lista con todas las provincias sin incluir el Id"""
    return repositorio.get_all_provincias(s)

@provincias_router.get('/{id}')
def get_by_id(id: int, s:Session = Depends(get_session)):
    provincia = repositorio.provincia_por_id(id,s)
    if provincia is None:
        raise HTTPException(status_code=404,detail="Provincia No Encontrada")
    return provincia

@provincias_router.get('/Buscar/{nombre}')
def get_by_nombre(nombre:str, s:Session = Depends(get_session)):
    return repositorio.provincia_por_nombre(nombre,s)

@provincias_router.post('/',response_model=ProvinciaApi)
def agregar(datos: ProvinciaSinId, s:Session = Depends(get_session)):
    provincia = repositorio.agregar(datos,s)
    return provincia

@provincias_router.delete('/{id}')
def borrar(id: int, s:Session = Depends(get_session)):
    repositorio.borrar(id, s)
    return 'Provincia Borrada'

@provincias_router.put('/{id}', response_model=ProvinciaApi)
def actualizar(id:int, datos:ProvinciaSinId, s:Session=Depends(get_session)):
   provincia =  repositorio.actualizar(id, datos, s)
   return provincia
