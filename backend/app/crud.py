# backend/app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.exc import IntegrityError
from datetime import datetime


# ==== Crear un usuario ====
def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(nombre=usuario.nombre, email=usuario.email, tipo=usuario.tipo)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


# ==== Obtener todos los usuarios ====
def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()


# ==== Crear un profesional ====
def create_profesional(db: Session, profesional: schemas.ProfesionalCreate):
    db_profesional = models.Profesional(
        id_usuario=profesional.id_usuario,
        oficio=profesional.oficio,
        verificacion=profesional.verificacion,
        valoracion=profesional.valoracion
    )
    db.add(db_profesional)
    db.commit()
    db.refresh(db_profesional)
    return db_profesional


# ==== Obtener todos los profesionales ====
def get_profesionales(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Profesional).offset(skip).limit(limit).all()


# ==== Crear un servicio ====
def create_servicio(db: Session, servicio: schemas.ServicioCreate):
    db_servicio = models.Servicio(tipo=servicio.tipo, descripcion=servicio.descripcion, precio_base=servicio.precio_base)
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio


# ==== Obtener todos los servicios ====
def get_servicios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Servicio).offset(skip).limit(limit).all()


# ==== Crear un contrato ====
def create_contrato(db: Session, contrato: schemas.ContratoCreate):
    db_contrato = models.Contrato(
        id_cliente=contrato.id_cliente,
        id_profesional=contrato.id_profesional,
        fecha=contrato.fecha,
        estado=contrato.estado
    )
    db.add(db_contrato)
    db.commit()
    db.refresh(db_contrato)
    return db_contrato


# ==== Obtener todos los contratos ====
def get_contratos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contrato).offset(skip).limit(limit).all()


# ==== Crear una reseña ====
def create_resena(db: Session, reseña: schemas.ReseñaCreate):
    db_resena = models.Reseña(id_contrato=reseña.id_contrato, comentario=reseña.comentario, puntuacion=reseña.puntuacion)
    db.add(db_resena)
    db.commit()
    db.refresh(db_resena)
    return db_resena


# ==== Obtener todas las reseñas ====
def get_resenas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Reseña).offset(skip).limit(limit).all()
