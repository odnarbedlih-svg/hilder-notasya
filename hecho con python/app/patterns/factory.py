from typing import Dict, Any
from app.dtos.estudiante_dto import EstudianteCreateDTO
from app.dtos.profesor_dto import ProfesorCreateDTO
from app.dtos.curso_dto import CursoCreateDTO

class DTOFactory:
    """
    Patrón Creacional: Factory Method
    Problema que resuelve: Centraliza y encapsula la instanciación y validación
    de esquemas DTO según el tipo de entidad requerida por la capa de presentación.
    """
    @staticmethod
    def create_dto(entity_type: str, data: Dict[str, Any]):
        entity_lower = entity_type.lower()
        if entity_lower == "estudiante":
            return EstudianteCreateDTO(**data)
        elif entity_lower == "profesor":
            return ProfesorCreateDTO(**data)
        elif entity_lower == "curso":
            return CursoCreateDTO(**data)
        else:
            raise ValueError(f"Tipo de entidad desconocido: '{entity_type}'")
