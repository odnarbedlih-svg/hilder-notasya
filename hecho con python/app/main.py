import time
import uuid
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from app.config.settings import get_settings
from app.config.database import engine, Base
from app.controllers import estudiante_router, profesor_router, curso_router
from app.controllers.analitica_controller import router as analitica_router
from app.views.dashboard_view import get_dashboard_html

# Inicializar tablas en base de datos
Base.metadata.create_all(bind=engine)

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description="""
    ### API RESTful de Gestión Académica - NOTASYA
    Desarrollado para la **Facultad de Ciencias e Ingeniería - Universidad de Manizales**.
    
    **Integrantes:**
    - Hildebrando Tangarife Cardona
    - Hildebrando Tangarife Cardona
    
    **Características:**
    - Arquitectura por capas (DTOs -> Controllers -> Services -> Repositories).
    - Patrones de Diseño (Singleton, Factory Method, Adapter, Strategy).
    - Principios SOLID.
    - Dashboard Web Reactivo integrado en `/` y `/dashboard`.
    - Middleware de Observabilidad (Header `X-Process-Time` y `X-Request-ID`).
    """,
    version="1.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# ----------------- MIDDLEWARE DE AUDITORÍA Y RENDIMIENTO -----------------
@app.middleware("http")
async def audit_and_performance_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start_time = time.perf_counter()
    
    response = await call_next(request)
    
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = f"{process_time:.4f}s"
    response.headers["X-Request-ID"] = request_id
    return response

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar Controladores
app.include_router(estudiante_router, prefix=settings.API_V1_PREFIX)
app.include_router(profesor_router, prefix=settings.API_V1_PREFIX)
app.include_router(curso_router, prefix=settings.API_V1_PREFIX)
app.include_router(analitica_router, prefix=settings.API_V1_PREFIX)

@app.get("/", response_class=HTMLResponse, tags=["Dashboard"], summary="Dashboard visual interactivo")
@app.get("/dashboard", response_class=HTMLResponse, tags=["Dashboard"], summary="Dashboard visual interactivo")
def serve_dashboard():
    return get_dashboard_html()

@app.get("/health", tags=["Health"], summary="Endpoint de estado de salud del sistema")
def health_check():
    return {
        "status": "online",
        "app_name": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "version": "1.1.0",
        "features": ["REST API", "Reactive Dashboard", "Academic Analytics", "Audit Middleware"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
