def greet():
    print("Hello")
    
hello = greet
hello()

avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

operations = {
    "average" : avg,
    "total" : total,
    "top" : top
}

students = [
    {"name" : "Akshat", "grades" : (67,90,95,100)},
    {"name" : "Mudit", "grades" : (76,92,97,100)},
    {"name" : "Mitika", "grades" : (79,80,99,98)},
    {"name" : "Rishita", "grades" : (57,90,95,100)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]
    
    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', or 'top': ")
    
    opeartion_function = operations[operation]
    print(opeartion_function(grades))