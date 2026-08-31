from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.config.database import get_db
from app.dtos.curso_dto import CursoCreateDTO, CursoUpdateDTO, CursoResponseDTO
from app.repositories.curso_repository import CursoRepository
from app.repositories.estudiante_repository import EstudianteRepository
from app.repositories.profesor_repository import ProfesorRepository
from app.services.curso_service import CursoService

router = APIRouter(prefix="/cursos", tags=["Cursos"])

def get_curso_service(db: Session = Depends(get_db)) -> CursoService:
    curso_repo = CursoRepository(db)
    est_repo = EstudianteRepository(db)
    prof_repo = ProfesorRepository(db)
    return CursoService(curso_repo, est_repo, prof_repo)

@router.get("", response_model=List[CursoResponseDTO], summary="Obtener todos los cursos")
def obtener_todos_los_cursos(service: CursoService = Depends(get_curso_service)):
    return service.obtener_todos_los_cursos()

@router.get("/{id}", response_model=CursoResponseDTO, summary="Obtener curso por ID")
def obtener_curso_por_id(id: int, service: CursoService = Depends(get_curso_service)):
    return service.obtener_curso_por_id(id)

@router.post("", response_model=CursoResponseDTO, status_code=status.HTTP_201_CREATED, summary="Crear curso")
def crear_curso(dto: CursoCreateDTO, service: CursoService = Depends(get_curso_service)):
    return service.crear_curso(dto)

@router.put("/{id}", response_model=CursoResponseDTO, summary="Actualizar curso")
def actualizar_curso(id: int, dto: CursoUpdateDTO, service: CursoService = Depends(get_curso_service)):
    return service.actualizar_curso(id, dto)
