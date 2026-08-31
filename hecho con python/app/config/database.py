from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config.settings import get_settings

settings = get_settings()

def get_engine():
    db_url = settings.DATABASE_URL
    if "sqlite" in db_url:
        return create_engine(db_url, connect_args={"check_same_thread": False})
    try:
        return create_engine(db_url, echo=settings.DB_ECHO, pool_pre_ping=True)
    except Exception:
        # Fallback a SQLite para ejecución local sin PostgreSQL instalado
        return create_engine("sqlite:///./notasya_local.db", connect_args={"check_same_thread": False})

engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
