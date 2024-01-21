class Employee:        
    def __init__(self,salary,age):
        self.salary = salary
        self.age= age
    
    organization = "WatchGuard"
            
    def display(self):
        print(f"Salary is {self.salary} and age is {self.age}")
        
    def __str__(self):
        return f"Hello! You are in self method"


e1 = Employee(20000,20)

e1.display()
Employee.display(e1)

print(getattr(e1,'age'))

setattr(e1,'salary',25000)

print(getattr(e1,'salary'))

e2 = e1

print(id(e1) == id(e2))

e3 = Employee(10000,19)
print(id(e2) == id(e3))

print(e1.organization)

e1.organization = "WatchGuard Technologies"

print(e1.organization)

Employee.organization = "WatchGuard Tech."

print(e1.organization)

print(e3.organization)

print(e1)