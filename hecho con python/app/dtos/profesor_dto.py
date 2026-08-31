from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class ProfesorBaseDTO(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=100, description="Nombre completo del profesor")
    tipo_identificacion: str = Field(..., min_length=2, max_length=10, description="Tipo de documento (CC, TI, CE, PAS)")
    numero_identificacion: str = Field(..., min_length=4, max_length=30, description="Número de documento de identidad único")
    especialidad: str = Field(..., min_length=2, max_length=100, description="Área o disciplina académica del docente")

class ProfesorCreateDTO(ProfesorBaseDTO):
    pass

class ProfesorUpdateDTO(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=100)
    tipo_identificacion: Optional[str] = Field(None, min_length=2, max_length=10)
    numero_identificacion: Optional[str] = Field(None, min_length=4, max_length=30)
    especialidad: Optional[str] = Field(None, min_length=2, max_length=100)

class ProfesorResponseDTO(ProfesorBaseDTO):
    id: int
    
    model_config = ConfigDict(from_attributes=True)
