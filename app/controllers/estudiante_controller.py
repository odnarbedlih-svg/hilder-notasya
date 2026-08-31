from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.config.database import get_db
from app.dtos.estudiante_dto import EstudianteCreateDTO, EstudianteUpdateDTO, EstudianteResponseDTO
from app.repositories.estudiante_repository import EstudianteRepository
from app.services.estudiante_service import EstudianteService

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])

def get_estudiante_service(db: Session = Depends(get_db)) -> EstudianteService:
    repo = EstudianteRepository(db)
    return EstudianteService(repo)

@router.get("", response_model=List[EstudianteResponseDTO], summary="Obtener todos los estudiantes")
def obtener_todos_los_estudiantes(service: EstudianteService = Depends(get_estudiante_service)):
    return service.obtener_todos_los_estudiantes()

@router.get("/{id}", response_model=EstudianteResponseDTO, summary="Obtener estudiante por ID")
def obtener_estudiante_por_id(id: int, service: EstudianteService = Depends(get_estudiante_service)):
    return service.obtener_estudiante_por_id(id)

@router.get("/correo/{correo}", response_model=EstudianteResponseDTO, summary="Obtener estudiante por Correo")
def obtener_estudiante_por_correo(correo: str, service: EstudianteService = Depends(get_estudiante_service)):
    return service.obtener_estudiante_por_correo(correo)

@router.post("", response_model=EstudianteResponseDTO, status_code=status.HTTP_201_CREATED, summary="Crear estudiante")
def crear_estudiante(dto: EstudianteCreateDTO, service: EstudianteService = Depends(get_estudiante_service)):
    return service.crear_estudiante(dto)

@router.put("/{id}", response_model=EstudianteResponseDTO, summary="Actualizar estudiante")
def actualizar_estudiante(id: int, dto: EstudianteUpdateDTO, service: EstudianteService = Depends(get_estudiante_service)):
    return service.actualizar_estudiante(id, dto)
