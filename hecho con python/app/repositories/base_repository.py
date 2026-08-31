from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional
from sqlalchemy.orm import Session

T = TypeVar('T')

class IBaseRepository(ABC, Generic[T]):
    @abstractmethod
    def get_all(self) -> List[T]:
        pass
        
    @abstractmethod
    def get_by_id(self, id_: int) -> Optional[T]:
        pass
        
    @abstractmethod
    def create(self, entity: T) -> T:
        pass
        
    @abstractmethod
    def update(self, entity: T) -> T:
        pass
