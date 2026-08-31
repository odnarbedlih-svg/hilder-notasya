from pydantic import BaseModel
from typing import List, Dict, Any

class ResumenAcademicoDTO(BaseModel):
    total_estudiantes: int
    total_profesores: int
    total_cursos: int
    promedio_general: float
    tasa_aprobacion_porcentaje: float
    estudiantes_con_honor: int
    cursos_por_estado: Dict[str, int]
