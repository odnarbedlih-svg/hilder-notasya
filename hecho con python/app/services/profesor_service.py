from typing import List
from fastapi import HTTPException, status
from app.models.profesor import Profesor
from app.dtos.profesor_dto import ProfesorCreateDTO, ProfesorUpdateDTO, ProfesorResponseDTO
from app.repositories.profesor_repository import ProfesorRepository

class ProfesorService:
    def __init__(self, repository: ProfesorRepository):
        self.repository = repository

    def obtener_todos_los_profesores(self) -> List[ProfesorResponseDTO]:
        profesores = self.repository.get_all()
        return [ProfesorResponseDTO.model_validate(p) for p in profesores]

    def obtener_profesor_por_id(self, profesor_id: int) -> ProfesorResponseDTO:
        profesor = self.repository.get_by_id(profesor_id)
        if not profesor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Profesor con ID {profesor_id} no encontrado"
            )
        return ProfesorResponseDTO.model_validate(profesor)

    def obtener_profesor_por_tipo_y_numero(self, tipo: str, numero: str) -> ProfesorResponseDTO:
        profesor = self.repository.get_by_identificacion(tipo, numero)
        if not profesor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Profesor con identificación {tipo}-{numero} no encontrado"
            )
        return ProfesorResponseDTO.model_validate(profesor)

    def crear_profesor(self, dto: ProfesorCreateDTO) -> ProfesorResponseDTO:
        if self.repository.get_by_identificacion(dto.tipo_identificacion, dto.numero_identificacion):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Ya existe un profesor con identificación {dto.tipo_identificacion}-{dto.numero_identificacion}"
            )
        
        nuevo_profesor = Profesor(
            nombre=dto.nombre,
            tipo_identificacion=dto.tipo_identificacion,
            numero_identificacion=dto.numero_identificacion,
            especialidad=dto.especialidad
        )
        guardado = self.repository.create(nuevo_profesor)
        return ProfesorResponseDTO.model_validate(guardado)

    def actualizar_profesor(self, profesor_id: int, dto: ProfesorUpdateDTO) -> ProfesorResponseDTO:
        profesor = self.repository.get_by_id(profesor_id)
        if not profesor:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Profesor con ID {profesor_id} no encontrado para actualizar"
            )
        
        if (dto.tipo_identificacion or dto.numero_identificacion):
            tipo = dto.tipo_identificacion or profesor.tipo_identificacion
            numero = dto.numero_identificacion or profesor.numero_identificacion
            existente = self.repository.get_by_identificacion(tipo, numero)
            if existente and existente.id != profesor_id:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"La identificación {tipo}-{numero} ya pertenece a otro profesor"
                )
            profesor.tipo_identificacion = tipo
            profesor.numero_identificacion = numero
            
        if dto.nombre is not None:
            profesor.nombre = dto.nombre
        if dto.especialidad is not None:
            profesor.especialidad = dto.especialidad

        actualizado = self.repository.update(profesor)
        return ProfesorResponseDTO.model_validate(actualizado)
