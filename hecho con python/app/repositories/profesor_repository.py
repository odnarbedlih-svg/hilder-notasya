from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.profesor import Profesor
from app.repositories.base_repository import IBaseRepository

class ProfesorRepository(IBaseRepository[Profesor]):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Profesor]:
        return self.db.query(Profesor).all()

    def get_by_id(self, id_: int) -> Optional[Profesor]:
        return self.db.query(Profesor).filter(Profesor.id == id_).first()

    def get_by_identificacion(self, tipo: str, numero: str) -> Optional[Profesor]:
        return self.db.query(Profesor).filter(
            Profesor.tipo_identificacion == tipo,
            Profesor.numero_identificacion == numero
        ).first()

    def create(self, entity: Profesor) -> Profesor:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update(self, entity: Profesor) -> Profesor:
        self.db.commit()
        self.db.refresh(entity)
        return entity
