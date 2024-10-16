from abc import ABC, abstractmethod

class AbstractCalculator(ABC):
    @abstractmethod
    def perform_calculation(self, operation):
        pass

    @abstractmethod
    def get_memory(self):
        pass