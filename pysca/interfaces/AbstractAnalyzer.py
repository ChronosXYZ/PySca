from abc import ABC, abstractmethod

class AbstractAnalyzer(ABC):
    @abstractmethod
    def analyze(self, result) -> object:
        pass