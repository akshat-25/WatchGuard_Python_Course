friends = {"Akshat","Mudit","Parakh"}

for friend in friends:
    print(friend)
    
elements = [0,1,2,3,4,5,6,7,8,9,10]

for index in elements:
    # print(f"{index} Hello World")
    print(str(index) + "   Hello World")
    
for index in range(2,20,3):
    print(index)
    
students = [
    {"name" : "Akshat", "grade" : 20},
    {"name" : "Mudit", "grade" : 10},
    {"name" : "Parakh", "grade" : 15},
]

for student in students:
    name = student["name"]
    grade = student["grade"]
    
    print(f"{name} has a grade of {grade}")