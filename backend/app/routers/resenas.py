# backend/app/routers/resenas.py

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

# ==== Crear una nueva reseña ====
@router.post("/resenas/", response_model=schemas.Reseña)
def create_resena(resena: schemas.ReseñaCreate, db: Session = Depends(get_db)):
    return crud.create_resena(db=db, reseña=resena)

# ==== Obtener todas las reseñas ====
@router.get("/resenas/", response_model=list[schemas.Reseña])
def get_resenas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    resenas = crud.get_resenas(db=db, skip=skip, limit=limit)
    return resenas
