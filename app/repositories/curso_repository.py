from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.curso import Curso
from app.repositories.base_repository import IBaseRepository

class CursoRepository(IBaseRepository[Curso]):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> List[Curso]:
        return self.db.query(Curso).all()

    def get_by_id(self, id_: int) -> Optional[Curso]:
        return self.db.query(Curso).filter(Curso.id == id_).first()

    def create(self, entity: Curso) -> Curso:
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity

    def update(self, entity: Curso) -> Curso:
        self.db.commit()
        self.db.refresh(entity)
        return entity
