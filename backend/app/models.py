# backend/app/models.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from .database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    tipo = Column(String, nullable=False)  # "cliente" o "profesional"

    profesional = relationship("Profesional", back_populates="usuario", uselist=False)
    contratos_cliente = relationship("Contrato", back_populates="cliente", foreign_keys="Contrato.id_cliente")

class Profesional(Base):
    __tablename__ = "profesionales"

    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    oficio = Column(String, nullable=False)
    verificacion = Column(String, default="pendiente")  # aprobado/rechazado
    valoracion = Column(Float, default=0.0)

    usuario = relationship("Usuario", back_populates="profesional")
    contratos = relationship("Contrato", back_populates="profesional")

class Servicio(Base):
    __tablename__ = "servicios"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)
    descripcion = Column(Text)
    precio_base = Column(Float, nullable=False)

class Contrato(Base):
    __tablename__ = "contratos"

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    id_profesional = Column(Integer, ForeignKey("profesionales.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    estado = Column(String, default="pendiente")  # pendiente, aceptado, finalizado, cancelado

    cliente = relationship("Usuario", back_populates="contratos_cliente", foreign_keys=[id_cliente])
    profesional = relationship("Profesional", back_populates="contratos")
    reseña = relationship("Reseña", back_populates="contrato", uselist=False)

class Reseña(Base):
    __tablename__ = "reseñas"

    id = Column(Integer, primary_key=True, index=True)
    id_contrato = Column(Integer, ForeignKey("contratos.id"), nullable=False)
    comentario = Column(Text)
    puntuacion = Column(Integer, nullable=False)

    contrato = relationship("Contrato", back_populates="reseña")
