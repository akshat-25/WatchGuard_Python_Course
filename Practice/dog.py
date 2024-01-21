class Dog:
    species = "Canis Familiaris"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name} is {self.age} years old"
   
    def speak(self,sound):
        return f"{self.name} barks: {sound}"
 
class JackRussellTerrier(Dog):
    def speak(self,sound="Arf"):
        return super().speak(sound)

class Duchshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Duchshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)


print(miles.species)
print(buddy.name)
print(jack)
print(type(miles))
print(miles.speak('Grrrr'))
print(jim.speak('Woof'))
