from app.patterns.singleton import DatabaseConnectionSingleton
from app.patterns.factory import DTOFactory
from app.patterns.adapter import ExternalEmailProviderSDK, EmailNotificationAdapter
from app.patterns.strategy import (
    StandardGradingStrategy, HonorsGradingStrategy, AcademicEvaluatorContext
)
from app.dtos.estudiante_dto import EstudianteCreateDTO

def test_singleton_database():
    s1 = DatabaseConnectionSingleton()
    s2 = DatabaseConnectionSingleton()
    assert s1 is s2, "Singleton debe devolver siempre la misma instancia"

def test_factory_method_dto():
    dto = DTOFactory.create_dto("estudiante", {
        "nombre": "Johntatan Sierra",
        "telefono": "3209876543",
        "correo": "johntatan@umanizales.edu.co"
    })
    assert isinstance(dto, EstudianteCreateDTO)
    assert dto.nombre == "Johntatan Sierra"

def test_adapter_pattern():
    sdk = ExternalEmailProviderSDK()
    adapter = EmailNotificationAdapter(sdk)
    result = adapter.send_notification("hilder@umanizales.edu.co", "Bienvenido a NOTASYA")
    assert result is True

def test_strategy_pattern():
    std_strategy = StandardGradingStrategy()
    honors_strategy = HonorsGradingStrategy()
    
    context = AcademicEvaluatorContext(std_strategy)
    eval_std = context.execute_evaluation(4.8)
    assert eval_std["status"] == "Aprobado"
    assert eval_std["honors"] is False
    
    # Cambiar estrategia dinámicamente
    context.set_strategy(honors_strategy)
    eval_honors = context.execute_evaluation(4.8)
    assert "Mención de Honor" in eval_honors["status"]
    assert eval_honors["honors"] is True
