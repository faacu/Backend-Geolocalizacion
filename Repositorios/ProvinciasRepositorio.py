from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, column
from Modelos.ProvinciaModelo import ProvinciaBd, ProvinciaSinId, ProvinciaApi

class Provinciarepo():
    def get_all_provincias(self, session: Session):
        return session.execute(select(ProvinciaBd)).scalars().all()

    def provincia_por_id(self, id:int, session:Session):
        return session.execute(select(ProvinciaBd).where(ProvinciaBd.id==id)).scalar()

    def provincia_por_nombre(self, nombre:str, session:Session):
        return session.execute(select(ProvinciaBd).where(column('pr_nombre').ilike(f'%{nombre}%'))).scalars().all()

    def agregar(self, datos:ProvinciaSinId, session:Session):
        instancia_bd = ProvinciaBd(pr_nombre = datos.pr_nombre, descripcion = datos.descripcion, id_pais = datos.id_pais)
        session.add(instancia_bd)
        session.commit()
        return instancia_bd

    def borrar(self, id:int, session:Session):
        instancia_bd = session.get(ProvinciaBd, id)
        if instancia_bd is None:
            raise HTTPException(status_code=400, detail='Provincia No Encontrada')
        try:
            session.delete(instancia_bd)
            session.commit()
        except:
            raise HTTPException(status_code=400, detail='No se puede borrar la provincia. Posiblemente esta referenciada por otro registro')
       

    def actualizar(self, id:int, datos:ProvinciaSinId, session:Session):
        instancia_bd = session.get(ProvinciaBd,id)
        if instancia_bd is None:
            raise HTTPException(status_code=400, detail='Provincia No Encontrada')
        try:
            instancia_bd.pr_nombre=datos.pr_nombre
            instancia_bd.descripcion=datos.descripcion
            instancia_bd.id_pais=datos.id_pais
            session.commit()
            
        except:
            raise HTTPException(status_code=400, detail='No se puede actualizar la provincia.')

        return instancia_bd
