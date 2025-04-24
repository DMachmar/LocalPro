# backend/app/routers/profesionales.py

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

# ==== Crear un nuevo profesional ====
@router.post("/profesionales/", response_model=schemas.Profesional)
def create_profesional(profesional: schemas.ProfesionalCreate, db: Session = Depends(get_db)):
    return crud.create_profesional(db=db, profesional=profesional)

# ==== Obtener todos los profesionales ====
@router.get("/profesionales/", response_model=list[schemas.Profesional])
def get_profesionales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    profesionales = crud.get_profesionales(db=db, skip=skip, limit=limit)
    return profesionales
