from abc import ABC, abstractmethod

class AbstractResultAction(ABC):
    @abstractmethod
    def handle(self, result):
        pass