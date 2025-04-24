# backend/app/schemas.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


# ==== Usuario ====
class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    tipo: str  # "cliente" o "profesional"

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioOut(UsuarioBase):
    id: int

    class Config:
        orm_mode = True


# ==== Profesional ====
class ProfesionalBase(BaseModel):
    oficio: str
    verificacion: Optional[str] = "pendiente"
    valoracion: Optional[float] = 0.0

class ProfesionalCreate(ProfesionalBase):
    id_usuario: int

class ProfesionalOut(ProfesionalBase):
    id: int
    id_usuario: int

    class Config:
        orm_mode = True


# ==== Servicio ====
class ServicioBase(BaseModel):
    tipo: str
    descripcion: Optional[str] = None
    precio_base: float

class ServicioCreate(ServicioBase):
    pass

class ServicioOut(ServicioBase):
    id: int

    class Config:
        orm_mode = True


# ==== Contrato ====
class ContratoBase(BaseModel):
    id_cliente: int
    id_profesional: int
    fecha: date
    estado: Optional[str] = "pendiente"

class ContratoCreate(ContratoBase):
    pass

class ContratoOut(ContratoBase):
    id: int

    class Config:
        orm_mode = True


# ==== Reseña ====
class ReseñaBase(BaseModel):
    id_contrato: int
    comentario: Optional[str] = None
    puntuacion: int

class ReseñaCreate(ReseñaBase):
    pass

class ReseñaOut(ReseñaBase):
    id: int

    class Config:
        orm_mode = True
