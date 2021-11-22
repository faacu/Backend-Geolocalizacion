from fastapi import FastAPI
import uvicorn
from db import create_all
from API.CiudadAPI import ciudades_router
from API.ProvinciaAPI import provincias_router
from API.PaisAPI import paises_router
from Modelos.CiudadModelo import CiudadBd
from Modelos.ProvinciaModelo import ProvinciaBd
from Modelos.PaisModelo import PaisBd
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3031",
    "localhost:3031"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(ciudades_router)
app.include_router(provincias_router)
app.include_router(paises_router)

create_all()

if __name__=='__main__':
    uvicorn.run('App:app', reload=True)
