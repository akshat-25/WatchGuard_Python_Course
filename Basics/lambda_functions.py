def divide(x,y):
    return x / y

a = divide(9,10) 

print(a)

multiply = lambda x, y: x * y
print(multiply(5,4))

my_student = {
    "name" : "Akshat",
    "grades" : [70,87,96,99]
}

average = lambda my_student : sum(my_student["grades"])/len(my_student["grades"])

print(average(my_student))
