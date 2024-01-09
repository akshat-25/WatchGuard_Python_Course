class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last
        
    def get_name(self):
        print(self.first)
        print(self.last)
        
    @classmethod
    def print_name(cls,one,two):
        return one+" "+two
        
    @staticmethod
    def name():
        print("Hello, I am a static method.")
        
        
emp1 = Employee('Akshat','Parakh')
emp1.get_name()

print(Employee.print_name('Hello','World'))

print(emp1.print_name("Called","Object"))

Employee.name()
emp1.name()