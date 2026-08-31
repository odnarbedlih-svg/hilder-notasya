import pytest
from pydantic import ValidationError
from app.dtos.estudiante_dto import EstudianteCreateDTO
from app.dtos.curso_dto import CursoCreateDTO

def test_estudiante_dto_valido():
    dto = EstudianteCreateDTO(
        nombre="Hildebrando Tangarife Cardona",
        telefono="3101234567",
        correo="htangarife@umanizales.edu.co"
    )
    assert dto.nombre == "Hildebrando Tangarife Cardona"
    assert dto.correo == "htangarife@umanizales.edu.co"

def test_estudiante_dto_correo_invalido():
    with pytest.raises(ValidationError):
        EstudianteCreateDTO(
            nombre="Hildebrando Tangarife Cardona",
            telefono="3101234567",
            correo="correo_no_valido"
        )

def test_curso_dto_calificacion_fuera_de_rango():
    with pytest.raises(ValidationError):
        CursoCreateDTO(
            nombre="Diseño de Sistemas",
            estudiante_id=1,
            profesor_id=1,
            calificacion=6.5 # Excede el límite de 5.0
        )
