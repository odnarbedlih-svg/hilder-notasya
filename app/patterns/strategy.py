from abc import ABC, abstractmethod
from typing import Dict, Any

class IGradingEvaluationStrategy(ABC):
    """
    Interfaz común para la estrategia de evaluación de calificaciones.
    """
    @abstractmethod
    def evaluate(self, grade: float) -> Dict[str, Any]:
        pass

class StandardGradingStrategy(IGradingEvaluationStrategy):
    """
    Estrategia de calificación estándar universitaria (Aprobado >= 3.0).
    """
    def evaluate(self, grade: float) -> Dict[str, Any]:
        is_passed = grade >= 3.0
        status = "Aprobado" if is_passed else "Reprobado"
        return {"grade": grade, "status": status, "honors": False}

class HonorsGradingStrategy(IGradingEvaluationStrategy):
    """
    Estrategia de calificación con distinción de honor (Excelente >= 4.5).
    """
    def evaluate(self, grade: float) -> Dict[str, Any]:
        is_passed = grade >= 3.0
        has_honors = grade >= 4.5
        status = "Excelente con Mención de Honor" if has_honors else ("Aprobado" if is_passed else "Reprobado")
        return {"grade": grade, "status": status, "honors": has_honors}

class AcademicEvaluatorContext:
    """
    Patrón de Comportamiento: Strategy
    Problema que resuelve: Permite cambiar dinámicamente las reglas y algoritmos
    de evaluación académica sin modificar la clase evaluadora en tiempo de ejecución.
    """
    def __init__(self, strategy: IGradingEvaluationStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: IGradingEvaluationStrategy):
        self._strategy = strategy

    def execute_evaluation(self, grade: float) -> Dict[str, Any]:
        return self._strategy.evaluate(grade)
