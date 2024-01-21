class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
        
    def __str__(self) -> str:
        return f'{self.color} car has {self.mileage}'
        
        
c1 = Car('blue',20000)
c2 = Car('red',30000)
print(c1)
print(c2)
