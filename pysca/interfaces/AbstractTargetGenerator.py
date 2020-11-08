from abc import ABC, abstractmethod

class AbstractTargetGenerator(ABC):
    @abstractmethod
    def next(self) -> object:
        raise NotImplemented

    @abstractmethod
    def configure(self, configuration):
        raise NotImplemented