from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, column
from Modelos.CiudadModelo import CiudadBd, CiudadSinId,CiudadApi


class Ciudadrepo():
    def get_all_ciudades(self, session: Session):
        return session.execute(select(CiudadBd)).scalars().all()

    def ciudad_por_id(self, id:int, session:Session):
        return session.execute(select(CiudadBd).where(CiudadBd.id==id)).scalar()

    def ciudad_por_nombre(self, nombre:str, session:Session):
        return session.execute(select(CiudadBd).where(column('ci_nombre').ilike(f'%{nombre}%'))).scalars().all()

    def agregar(self, datos:CiudadSinId, session:Session):
        instancia_bd = CiudadBd(ci_nombre = datos.ci_nombre,descripcion=datos.descripcion, id_provincia=datos.id_provincia)
        session.add(instancia_bd)
        session.commit()
        return instancia_bd

    def borrar(self, id:int, session:Session):
        instancia_bd = session.get(CiudadBd, id)
        if instancia_bd is None:
            raise HTTPException(status_code=400, detail='Ciudad no encontrada')
        try:
            session.delete(instancia_bd)
            session.commit()
        except:
            raise HTTPException(status_code=400, detail='No se puede borrar la ciudad')
       

    def actualizar(self, id:int, datos:CiudadSinId, session:Session):
        instancia_bd = session.get(CiudadBd,id)
        if instancia_bd is None:
            raise HTTPException(status_code=400, detail='Ciudad no encontrada')
        try:
            instancia_bd.ci_nombre=datos.ci_nombre
            instancia_bd.descripcion=datos.descripcion
            instancia_bd.id_provincia=datos.id_provincia

            session.commit()
            
        except:
            raise HTTPException(status_code=400, detail='No se puede actualizar la ciudad.')

        return instancia_bd
