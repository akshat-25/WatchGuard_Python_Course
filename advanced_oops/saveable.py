from abc import ABCMeta, abstractmethod
from database import Database


class Saveable:
    def save(self):
        Database.insert(self.to_dict())
        
    @abstractmethod
    def to_dict(self):
        pass