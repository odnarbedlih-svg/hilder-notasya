from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.main import app
from app.config.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_observability_middleware_headers():
    response = client.get("/health")
    assert "x-process-time" in response.headers
    assert "x-request-id" in response.headers

def test_flujo_completo_notasya():
    # 1. Crear Estudiante
    est_resp = client.post("/api/v1/estudiantes", json={
        "nombre": "Hildebrando Tangarife Cardona",
        "telefono": "3101234567",
        "correo": "htangarife@umanizales.edu.co"
    })
    assert est_resp.status_code == 201
    est_id = est_resp.json()["id"]

    # 2. Crear Profesor
    prof_resp = client.post("/api/v1/profesores", json={
        "nombre": "Dr. Jorge Aguirre",
        "tipo_identificacion": "CC",
        "numero_identificacion": "1053800900",
        "especialidad": "Arquitectura de Software"
    })
    assert prof_resp.status_code == 201
    prof_id = prof_resp.json()["id"]

    # 3. Crear Curso
    curso_resp = client.post("/api/v1/cursos", json={
        "nombre": "Diseño de Sistemas de Información",
        "estudiante_id": est_id,
        "profesor_id": prof_id,
        "calificacion": 5.0
    })
    assert curso_resp.status_code == 201
    assert curso_resp.json()["calificacion"] == 5.0

    # 4. Consultar Estudiante por Correo
    get_correo_resp = client.get("/api/v1/estudiantes/correo/htangarife@umanizales.edu.co")
    assert get_correo_resp.status_code == 200
    assert get_correo_resp.json()["nombre"] == "Hildebrando Tangarife Cardona"

    # 5. Probar Regla de Negocio: Correo Duplicado (409 Conflict)
    dup_resp = client.post("/api/v1/estudiantes", json={
        "nombre": "Otro Estudiante",
        "telefono": "3119998877",
        "correo": "htangarife@umanizales.edu.co"
    })
    assert dup_resp.status_code == 409

    # 6. Probar Endpoint de Analítica Académica
    analitica_resp = client.get("/api/v1/analitica/resumen")
    assert analitica_resp.status_code == 200
    data = analitica_resp.json()
    assert data["total_estudiantes"] >= 1
    assert data["total_profesores"] >= 1
    assert data["promedio_general"] == 5.0
