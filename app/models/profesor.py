from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Profesor(Base):
    __tablename__ = "profesores"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    tipo_identificacion = Column(String(10), nullable=False) # CC, TI, CE, Pasaporte
    numero_identificacion = Column(String(30), unique=True, index=True, nullable=False)
    especialidad = Column(String(100), nullable=False)
    
    # Relación uno a muchos con Curso
    cursos = relationship("Curso", back_populates="profesor", cascade="all, delete-orphan")
