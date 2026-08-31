from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional

class EstudianteBaseDTO(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100, description="Nombre completo del estudiante")
    telefono: str = Field(..., min_length=7, max_length=20, description="Número de teléfono de contacto")
    correo: EmailStr = Field(..., description="Correo electrónico único y válido")

class EstudianteCreateDTO(EstudianteBaseDTO):
    pass

class EstudianteUpdateDTO(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=100)
    telefono: Optional[str] = Field(None, min_length=7, max_length=20)
    correo: Optional[EmailStr] = None

class EstudianteResponseDTO(EstudianteBaseDTO):
    id: int
    
    model_config = ConfigDict(from_attributes=True)
