from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from app.dtos.estudiante_dto import EstudianteResponseDTO
from app.dtos.profesor_dto import ProfesorResponseDTO

class CursoBaseDTO(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100, description="Nombre de la asignatura o curso")
    estudiante_id: int = Field(..., gt=0, description="Identificador del estudiante matriculado")
    profesor_id: int = Field(..., gt=0, description="Identificador del profesor titular")
    calificacion: float = Field(..., ge=0.0, le=5.0, description="Nota numérica del curso en escala de 0.0 a 5.0")

class CursoCreateDTO(CursoBaseDTO):
    pass

class CursoUpdateDTO(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=100)
    estudiante_id: Optional[int] = Field(None, gt=0)
    profesor_id: Optional[int] = Field(None, gt=0)
    calificacion: Optional[float] = Field(None, ge=0.0, le=5.0)

class CursoResponseDTO(BaseModel):
    id: int
    nombre: str
    estudiante_id: int
    profesor_id: int
    calificacion: float
    estudiante: Optional[EstudianteResponseDTO] = None
    profesor: Optional[ProfesorResponseDTO] = None
    
    model_config = ConfigDict(from_attributes=True)
