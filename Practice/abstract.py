from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        None
    
    def cpu(self):
        print("In the CPU function")
        
              
class Laptop(Computer):
    def process(self):
        print("In the process method")

c1 = Laptop()
c1.process()
c1.cpu()