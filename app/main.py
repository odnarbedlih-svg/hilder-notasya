from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import get_settings
from app.config.database import engine, Base
from app.controllers import estudiante_router, profesor_router, curso_router

# Inicializar tablas en base de datos
Base.metadata.create_all(bind=engine)

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description="""
    ### API RESTful de Gestión Académica - NOTASYA
    Desarrollado para la **Facultad de Ciencias e Ingeniería - Universidad de Manizales**.
    
    **Integrantes:**
    - Hilder Tangarife
    - Johntatan Sierra
    
    **Características:**
    - Arquitectura por capas (DTOs -> Controllers -> Services -> Repositories).
    - Patrones de Diseño (Singleton, Factory Method, Adapter, Strategy).
    - Principios SOLID.
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

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

@app.get("/health", tags=["Health"], summary="Endpoint de estado de salud")
def health_check():
    return {
        "status": "online",
        "app_name": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
