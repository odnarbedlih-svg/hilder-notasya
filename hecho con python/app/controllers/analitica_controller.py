from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.dtos.analitica_dto import ResumenAcademicoDTO
from app.services.analitica_service import AnaliticaAcademicaService

router = APIRouter(prefix="/analitica", tags=["Analítica Académica"])

@router.get("/resumen", response_model=ResumenAcademicoDTO, summary="Obtener métricas y KPIs académicos globales")
def obtener_resumen(db: Session = Depends(get_db)):
    service = AnaliticaAcademicaService(db)
    return service.obtener_resumen_academico()
