from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Optional
from app.config.settings import get_settings

class DatabaseConnectionSingleton:
    """
    Patrón Creacional: Singleton
    Problema que resuelve: Garantiza una única instancia del motor de base de datos
    y pool de conexiones para evitar sobrecarga y fuga de recursos en PostgreSQL.
    """
    _instance: Optional['DatabaseConnectionSingleton'] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnectionSingleton, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        settings = get_settings()
        self.engine = create_engine(
            settings.DATABASE_URL,
            echo=settings.DB_ECHO,
            pool_pre_ping=True
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self) -> Session:
        return self.SessionLocal()
