from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, column
from Modelos.PaisModelo import PaisBd, PaisSinId, PaisApi

class Paisrepo():
    def get_all_paises(self, session: Session):
        return session.execute(select(PaisBd)).scalars().all()

    def pais_por_nombre(self, nombre:str, session:Session):
        return session.execute(select(PaisBd).where(column('pa_nombre').ilike(f'%{nombre}%'))).scalars().all()

    def agregar(self, datos:PaisSinId, session:Session):
        instancia_bd = PaisBd(pa_nombre = datos.pa_nombre, cantidadHabitantes = datos.cantidadHabitantes)
        session.add(instancia_bd)
        session.commit()
        return instancia_bd

    def borrar(self, id:int, session:Session):
        instancia_bd = session.get(PaisBd, id)
        if instancia_bd is None:
            raise HTTPException(status_code=400, detail='Pais No Encontrado')
        try:
            session.delete(instancia_bd)
            session.commit()
        except:
            raise HTTPException(status_code=400, detail='No se puede borrar el pais. Posiblemente esta referenciada por otro registro')
       

    def actualizar(self, id:int, datos:PaisSinId, session:Session):
        instancia_bd = session.get(PaisBd,id)
        if instancia_bd is None:
            raise HTTPException(status_code=400, detail='Pais No Encontrado')
        try:
            instancia_bd.pa_nombre=datos.pa_nombre
            instancia_bd.cantidadHabitantes=datos.cantidadHabitantes
            session.commit()
            
        except:
            raise HTTPException(status_code=400, detail='No se puede actualizar el pais.')

        return instancia_bd
