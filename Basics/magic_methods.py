# __repr__ method is used to return a string representation of the instance
# in a format that can be used to recreate the object

# __str__ method is used to return a string representation of the instance
# in a human readable format 

class Garage():
    def __init__(self):
        self.cars = []
        
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self,num):
        return self.cars[num]
    
    def __repr__(self):
        return f"Garage()"
    
    def __str__(self):
        return f'<Garage with {len(self)} cars.>'
    
ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Discovery')

# print(len(ford))

# print(ford[1]) # Garage.__getitem__(ford,1)

for car in ford:
    print(car)

print(ford.__len__())

print(repr(ford))
print(ford.__str__())
maruti = eval(repr(ford))

print(len(maruti))
