from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URI = "postgresql+psycopg2://postgres:dfgedc@localhost:5432/geolocalizacion"

engine = create_engine(DATABASE_URI, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_all():
    print("Creando tablas",Base)
    Base.metadata.create_all(bind=engine)

def drop_all():
    Base.metadata.drop_all(bind=engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
