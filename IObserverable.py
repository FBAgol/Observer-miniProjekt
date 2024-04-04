#Interface Observerable
from abc import ABC, abstractmethod
class IObserverable(ABC): 
    @abstractmethod
    def addObserver(self,observer):
        pass

    @abstractmethod
    def removeObserver(self, observer):
        pass
    
    @abstractmethod
    def notify_observers(self, data):
        pass



#Interface for Observer

class IObserver(ABC):
    
    @abstractmethod
    def update(self, data):
        pass

        

