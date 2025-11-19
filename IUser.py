from abc import ABC, abstractmethod

class IUser(ABC):
    @abstractmethod
    def describe(self):
        pass
