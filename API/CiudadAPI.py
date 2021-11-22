from fastapi import APIRouter, Depends
from db import get_session 
from sqlalchemy.orm import Session
from Repositorios.CiudadesRepositorio import Ciudadrepo
from Modelos.CiudadModelo import CiudadSinId, CiudadApi, CiudadBd
from typing import List
from fastapi.exceptions import HTTPException


ciudades_router = APIRouter(prefix='/ciudades', tags=['Ciudades'])
repositorio = Ciudadrepo()

@ciudades_router.get('/')
def get_all(s: Session = Depends(get_session)):
    return repositorio.get_all_ciudades(s)

@ciudades_router.get('/Buscar/{nombre}')
def get_by_nombre(nombre:str, s:Session = Depends(get_session)):
    return repositorio.ciudad_por_nombre(nombre,s)

@ciudades_router.get('/{id}')
def get_by_id(id: int, s:Session = Depends(get_session)):
    ciudad = repositorio.ciudad_por_id(id,s)
    if ciudad is None:
        raise HTTPException(status_code=404,detail="Ciudad No Encontrada")
    return ciudad

@ciudades_router.post('/',response_model=CiudadApi)
def agregar(datos: CiudadSinId, s:Session = Depends(get_session)):
    ciudad = repositorio.agregar(datos,s)
    return ciudad

@ciudades_router.delete('/{id}')
def borrar(id: int, s:Session = Depends(get_session)):
    repositorio.borrar(id, s)
    return 'Se borro la ciudad'

@ciudades_router.put('/{id}', response_model=CiudadApi)
def actualizar(id:int, datos:CiudadSinId, s:Session=Depends(get_session)):
   ciudad =  repositorio.actualizar(id, datos, s)
   return ciudad
