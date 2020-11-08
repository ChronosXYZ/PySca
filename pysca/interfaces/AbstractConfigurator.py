from abc import ABC, abstractmethod

class AbstractConfigurator(ABC):
    @abstractmethod
    def configure(self, input) -> object:
        pass