from sqlalchemy.orm import Session
from app.models.estudiante import Estudiante
from app.models.profesor import Profesor
from app.models.curso import Curso
from app.patterns.strategy import HonorsGradingStrategy, AcademicEvaluatorContext
from app.dtos.analitica_dto import ResumenAcademicoDTO

class AnaliticaAcademicaService:
    """
    Servicio de inteligencia analítica académica.
    Aplica el patrón Strategy para evaluar el rendimiento global de la institución.
    """
    def __init__(self, db: Session):
        self.db = db
        self.evaluator = AcademicEvaluatorContext(HonorsGradingStrategy())

    def obtener_resumen_academico(self) -> ResumenAcademicoDTO:
        total_est = self.db.query(Estudiante).count()
        total_prof = self.db.query(Profesor).count()
        cursos = self.db.query(Curso).all()
        total_cursos = len(cursos)

        if total_cursos == 0:
            return ResumenAcademicoDTO(
                total_estudiantes=total_est,
                total_profesores=total_prof,
                total_cursos=0,
                promedio_general=0.0,
                tasa_aprobacion_porcentaje=0.0,
                estudiantes_con_honor=0,
                cursos_por_estado={"Aprobado": 0, "Reprobado": 0, "Mención de Honor": 0}
            )

        suma_notas = sum(c.calificacion for c in cursos)
        promedio = round(suma_notas / total_cursos, 2)

        aprobados = 0
        con_honor = 0
        reprobados = 0

        for c in cursos:
            res = self.evaluator.execute_evaluation(c.calificacion)
            if res["honors"]:
                con_honor += 1
                aprobados += 1
            elif res["grade"] >= 3.0:
                aprobados += 1
            else:
                reprobados += 1

        tasa_aprob = round((aprobados / total_cursos) * 100, 1)

        return ResumenAcademicoDTO(
            total_estudiantes=total_est,
            total_profesores=total_prof,
            total_cursos=total_cursos,
            promedio_general=promedio,
            tasa_aprobacion_porcentaje=tasa_aprob,
            estudiantes_con_honor=con_honor,
            cursos_por_estado={
                "Aprobados": aprobados,
                "Reprobados": reprobados,
                "Con Mención de Honor": con_honor
            }
        )
