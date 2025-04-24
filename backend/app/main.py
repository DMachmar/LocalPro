from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models, schemas
from .. import crud
from .database import SessionLocal, engine

# backend/app/main.py

from fastapi import FastAPI
from .routers import usuarios, profesionales, servicios, contratos, resenas

app = FastAPI()

# Incluyendo los routers en las rutas
app.include_router(usuarios.router)
app.include_router(profesionales.router)
app.include_router(servicios.router)
app.include_router(contratos.router)
app.include_router(resenas.router)

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="LocalPro API")

# Dependencia para obtener sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints básicos

@app.post("/usuarios/", response_model=schemas.UsuarioOut)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.crear_usuario(db, usuario)

@app.post("/profesionales/", response_model=schemas.ProfesionalOut)
def crear_profesional(profesional: schemas.ProfesionalCreate, db: Session = Depends(get_db)):
    return crud.crear_profesional(db, profesional)

@app.post("/servicios/", response_model=schemas.ServicioOut)
def crear_servicio(servicio: schemas.ServicioCreate, db: Session = Depends(get_db)):
    return crud.crear_servicio(db, servicio)

@app.post("/contratos/", response_model=schemas.ContratoOut)
def crear_contrato(contrato: schemas.ContratoCreate, db: Session = Depends(get_db)):
    return crud.crear_contrato(db, contrato)

@app.post("/resenas/", response_model=schemas.ResenaOut)
def crear_resena(resena: schemas.ResenaCreate, db: Session = Depends(get_db)):
    return crud.crear_resena(db, resena)

# Puedes agregar endpoints GET para listar cada entidad también.
