# backend/app/routers/contratos.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ==== Crear un nuevo contrato ====
@router.post("/contratos/", response_model=schemas.Contrato)
def create_contrato(contrato: schemas.ContratoCreate, db: Session = Depends(get_db)):
    return crud.create_contrato(db=db, contrato=contrato)

# ==== Obtener todos los contratos ====
@router.get("/contratos/", response_model=list[schemas.Contrato])
def get_contratos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contratos = crud.get_contratos(db=db, skip=skip, limit=limit)
    return contratos
