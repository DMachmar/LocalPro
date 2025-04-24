# backend/app/routers/servicios.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ... import crud, models, schemas
from ..database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ==== Crear un nuevo servicio ====
@router.post("/servicios/", response_model=schemas.Servicio)
def create_servicio(servicio: schemas.ServicioCreate, db: Session = Depends(get_db)):
    return crud.create_servicio(db=db, servicio=servicio)

# ==== Obtener todos los servicios ====
@router.get("/servicios/", response_model=list[schemas.Servicio])
def get_servicios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    servicios = crud.get_servicios(db=db, skip=skip, limit=limit)
    return servicios
