from abc import ABC, abstractmethod

class AbstractFilter(ABC):
    @abstractmethod
    def filter(self, result) -> object:
        pass