from typing import List
from fastapi import HTTPException, status
from app.models.estudiante import Estudiante
from app.dtos.estudiante_dto import EstudianteCreateDTO, EstudianteUpdateDTO, EstudianteResponseDTO
from app.repositories.estudiante_repository import EstudianteRepository

class EstudianteService:
    def __init__(self, repository: EstudianteRepository):
        self.repository = repository

    def obtener_todos_los_estudiantes(self) -> List[EstudianteResponseDTO]:
        estudiantes = self.repository.get_all()
        return [EstudianteResponseDTO.model_validate(e) for e in estudiantes]

    def obtener_estudiante_por_id(self, estudiante_id: int) -> EstudianteResponseDTO:
        estudiante = self.repository.get_by_id(estudiante_id)
        if not estudiante:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Estudiante con ID {estudiante_id} no encontrado"
            )
        return EstudianteResponseDTO.model_validate(estudiante)

    def obtener_estudiante_por_correo(self, correo: str) -> EstudianteResponseDTO:
        estudiante = self.repository.get_by_correo(correo)
        if not estudiante:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Estudiante con correo '{correo}' no encontrado"
            )
        return EstudianteResponseDTO.model_validate(estudiante)

    def crear_estudiante(self, dto: EstudianteCreateDTO) -> EstudianteResponseDTO:
        # Validación de regla de negocio: Correo único
        if self.repository.get_by_correo(dto.correo):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Ya existe un estudiante registrado con el correo '{dto.correo}'"
            )
        
        nuevo_estudiante = Estudiante(
            nombre=dto.nombre,
            telefono=dto.telefono,
            correo=dto.correo
        )
        guardado = self.repository.create(nuevo_estudiante)
        return EstudianteResponseDTO.model_validate(guardado)

    def actualizar_estudiante(self, estudiante_id: int, dto: EstudianteUpdateDTO) -> EstudianteResponseDTO:
        estudiante = self.repository.get_by_id(estudiante_id)
        if not estudiante:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Estudiante con ID {estudiante_id} no encontrado para actualizar"
            )
        
        if dto.correo and dto.correo != estudiante.correo:
            if self.repository.get_by_correo(dto.correo):
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"El correo '{dto.correo}' ya está en uso por otro estudiante"
                )
            estudiante.correo = dto.correo
            
        if dto.nombre is not None:
            estudiante.nombre = dto.nombre
        if dto.telefono is not None:
            estudiante.telefono = dto.telefono

        actualizado = self.repository.update(estudiante)
        return EstudianteResponseDTO.model_validate(actualizado)
