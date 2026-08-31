from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.estudiante import Estudiante
from app.repositories.base_repository import IBaseRepository

class EstudianteRepository(IBaseRepository[Estudiante]):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Estudiante]:
        return self.db.query(Estudiante).all()

    def get_by_id(self, id_: int) -> Optional[Estudiante]:
        return self.db.query(Estudiante).filter(Estudiante.id == id_).first()

    def get_by_correo(self, correo: str) -> Optional[Estudiante]:
        return self.db.query(Estudiante).filter(Estudiante.correo == correo).first()

    def create(self, entity: Estudiante) -> Estudiante:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update(self, entity: Estudiante) -> Estudiante:
        self.db.commit()
        self.db.refresh(entity)
        return entity
