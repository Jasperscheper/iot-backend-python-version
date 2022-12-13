from abc import ABC, abstractmethod

class RepositoryInterface(ABC):
    @abstractmethod
    def insert():
        pass
    @abstractmethod
    def fetch():
        pass
    @abstractmethod
    def fetchAll():
        pass
    
    @abstractmethod
    def delete():
        pass