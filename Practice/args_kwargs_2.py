class Car:
    def __init__(self,*args):
        self.speed = args[0]
        self.color = args[1]
        
        
audi = Car(200,'red')
bmw = Car(300,'black')

print(audi.color)
print(bmw.speed)


class Carr:
    def __init__(self,**kwargs):
        self.speed = kwargs['s']
        self.color = kwargs['c']
        
porche = Carr(s=350,c ="white")

print(porche.color)