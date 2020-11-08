from abc import ABC, abstractmethod

class AbstractFilter(ABC):
    @abstractmethod
    def analyze(self, result) -> object:
        pass