class Employee:
    dept = 'IT'  # class variables
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
emp1 = Employee('akshat','101')
emp2 = Employee('Milind','102')

# print(emp1.dept)
# print(emp2.dept)
# print(emp1.name)
# print(emp2.name)
# print(emp1.id)
# print(emp2.id)

print(emp1.name)

print(Employee.dept)
emp1.name = 'Networking'
emp1.dept = "Admin"
print(emp1.dept)
print(emp2.dept)

Employee.dept = "Database Administration"
print(emp1.dept)
print(emp2.dept)


class Car:
    num = 7
    msg = "This is a good Car"
    
obj = Car()

print(Car.num)
print(Car.msg)

print(obj.num)
print(obj.msg)



