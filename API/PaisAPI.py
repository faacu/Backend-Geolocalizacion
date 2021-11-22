from fastapi import APIRouter, Depends
from db import get_session
from sqlalchemy.orm import Session
from Repositorios.PaisRepositorio import Paisrepo
from Modelos.PaisModelo import PaisSinId, PaisApi
from typing import List
from Modelos.PaisModelo import PaisBd
from fastapi.exceptions import HTTPException


paises_router = APIRouter(prefix='/paises', tags=['Paises'])
repositorio = Paisrepo()

@paises_router.get('/')
def get_all(s: Session = Depends(get_session)):
    return repositorio.get_all_paises(s)

@paises_router.get('/Buscar/{nombre}')
def get_by_nombre(nombre:str, s:Session = Depends(get_session)):
    return repositorio.pais_por_nombre(nombre,s)

@paises_router.get('/{id}')
def get_by_id(id: int, s:Session = Depends(get_session)):
    pais = repositorio.pais_por_id(id,s)
    if pais is None:
        raise HTTPException(status_code=404,detail="Pais No Encontrado")
    return pais

@paises_router.post('/',response_model=PaisApi)
def agregar(datos: PaisSinId, s:Session = Depends(get_session)):
    pais = repositorio.agregar(datos,s)
    return pais

@paises_router.delete('/{id}')
def borrar(id: int, s:Session = Depends(get_session)):
    repositorio.borrar(id, s)
    return 'Pais Borrado'

@paises_router.put('/{id}', response_model=PaisApi)
def actualizar(id:int, datos:PaisSinId, s:Session=Depends(get_session)):
   pais =  repositorio.actualizar(id, datos, s)
   return pais
