from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.config.database import get_db
from app.dtos.profesor_dto import ProfesorCreateDTO, ProfesorUpdateDTO, ProfesorResponseDTO
from app.repositories.profesor_repository import ProfesorRepository
from app.services.profesor_service import ProfesorService

router = APIRouter(prefix="/profesores", tags=["Profesores"])

def get_profesor_service(db: Session = Depends(get_db)) -> ProfesorService:
    repo = ProfesorRepository(db)
    return ProfesorService(repo)

@router.get("", response_model=List[ProfesorResponseDTO], summary="Obtener todos los profesores")
def obtener_todos_los_profesores(service: ProfesorService = Depends(get_profesor_service)):
    return service.obtener_todos_los_profesores()

@router.get("/{id}", response_model=ProfesorResponseDTO, summary="Obtener profesor por ID")
def obtener_profesor_por_id(id: int, service: ProfesorService = Depends(get_profesor_service)):
    return service.obtener_profesor_por_id(id)

@router.get("/identificacion/{tipo}/{numero}", response_model=ProfesorResponseDTO, summary="Obtener profesor por Tipo y Número de Identificación")
def obtener_profesor_por_tipo_y_numero(tipo: str, numero: str, service: ProfesorService = Depends(get_profesor_service)):
    return service.obtener_profesor_por_tipo_y_numero(tipo, numero)

@router.post("", response_model=ProfesorResponseDTO, status_code=status.HTTP_201_CREATED, summary="Crear profesor")
def crear_profesor(dto: ProfesorCreateDTO, service: ProfesorService = Depends(get_profesor_service)):
    return service.crear_profesor(dto)

@router.put("/{id}", response_model=ProfesorResponseDTO, summary="Actualizar profesor")
def actualizar_profesor(id: int, dto: ProfesorUpdateDTO, service: ProfesorService = Depends(get_profesor_service)):
    return service.actualizar_profesor(id, dto)
