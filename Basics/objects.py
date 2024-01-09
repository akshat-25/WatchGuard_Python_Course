class Student:
    def __init__(self,new_name,new_grades):  # It is DUNDER FUNCTION / CONSTRUCTOR
        # self refers to the current object.
        self.name = new_name # Property
        self.grades = new_grades
        
    def average(self):
        return sum(self.grades)/len(self.grades)

      
student_one = Student("Akshat Parakh",[99,98,96,99])
print(student_one.name)
print(student_one.grades)

avg = student_one.average()

print(avg)
print(Student.average(student_one))