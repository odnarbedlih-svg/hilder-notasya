from typing import List
from fastapi import HTTPException, status
from app.models.curso import Curso
from app.dtos.curso_dto import CursoCreateDTO, CursoUpdateDTO, CursoResponseDTO
from app.repositories.curso_repository import CursoRepository
from app.repositories.estudiante_repository import EstudianteRepository
from app.repositories.profesor_repository import ProfesorRepository

class CursoService:
    def __init__(
        self,
        curso_repo: CursoRepository,
        estudiante_repo: EstudianteRepository,
        profesor_repo: ProfesorRepository
    ):
        self.curso_repo = curso_repo
        self.estudiante_repo = estudiante_repo
        self.profesor_repo = profesor_repo

    def obtener_todos_los_cursos(self) -> List[CursoResponseDTO]:
        cursos = self.curso_repo.get_all()
        return [CursoResponseDTO.model_validate(c) for c in cursos]

    def obtener_curso_por_id(self, curso_id: int) -> CursoResponseDTO:
        curso = self.curso_repo.get_by_id(curso_id)
        if not curso:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Curso con ID {curso_id} no encontrado"
            )
        return CursoResponseDTO.model_validate(curso)

    def crear_curso(self, dto: CursoCreateDTO) -> CursoResponseDTO:
        # Validación de regla de negocio: Estudiante debe existir
        if not self.estudiante_repo.get_by_id(dto.estudiante_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No se puede crear el curso. El estudiante con ID {dto.estudiante_id} no existe."
            )
        # Validación de regla de negocio: Profesor debe existir
        if not self.profesor_repo.get_by_id(dto.profesor_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No se puede crear el curso. El profesor con ID {dto.profesor_id} no existe."
            )
            
        nuevo_curso = Curso(
            nombre=dto.nombre,
            estudiante_id=dto.estudiante_id,
            profesor_id=dto.profesor_id,
            calificacion=dto.calificacion
        )
        guardado = self.curso_repo.create(nuevo_curso)
        return CursoResponseDTO.model_validate(guardado)

    def actualizar_curso(self, curso_id: int, dto: CursoUpdateDTO) -> CursoResponseDTO:
        curso = self.curso_repo.get_by_id(curso_id)
        if not curso:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Curso con ID {curso_id} no encontrado para actualizar"
            )
            
        if dto.estudiante_id is not None:
            if not self.estudiante_repo.get_by_id(dto.estudiante_id):
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"El estudiante con ID {dto.estudiante_id} no existe"
                )
            curso.estudiante_id = dto.estudiante_id
            
        if dto.profesor_id is not None:
            if not self.profesor_repo.get_by_id(dto.profesor_id):
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"El profesor con ID {dto.profesor_id} no existe"
                )
            curso.profesor_id = dto.profesor_id
            
        if dto.nombre is not None:
            curso.nombre = dto.nombre
        if dto.calificacion is not None:
            curso.calificacion = dto.calificacion

        actualizado = self.curso_repo.update(curso)
        return CursoResponseDTO.model_validate(actualizado)
