from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(20), nullable=False)
    correo = Column(String(100), unique=True, index=True, nullable=False)
    
    # Relación uno a muchos con Curso
    cursos = relationship("Curso", back_populates="estudiante", cascade="all, delete-orphan")
