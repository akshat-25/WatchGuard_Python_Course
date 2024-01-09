class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)
    
class WorkingStudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary = salary
    
    @property # We should use this only when the function calculates some values
    def weekly_salary(self):
        return self.salary * 37.5
    
akshat = WorkingStudent("Akshat","SKIT",45.56)
print(akshat.name)
print(akshat.school)
print(akshat.salary)

akshat.marks.append(99)
akshat.marks.append(95)

print(akshat.average())
print(akshat.weekly_salary)

millu = Student("Millu", "JECRC")
print(millu.name)