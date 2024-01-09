print("Hello World!!!")
age = 22

print(age + 30)

print(type(age))

f = 1.23456

print(type(f))

maths_operations = 1 + 2 / 4 * 5 - 2; 
# Whenever we do division in python, we get answer in float by default

print(maths_operations)

integer_division = 12 // 3

print(integer_division)

a = 17.5
b = 5

c = a + b - 9

print(c)

my_string = "Akshat"

string_with_quotes = 'He said "You are amazing!" yesterday..'

print(string_with_quotes)

"""
This is a multiline comment
"""
age_as_str = str(age)
print("Hello Akshat " + age_as_str)

# String interpolation example....
x = f"Akshat age is {age}"

name = "Akshat"

final_greeting = "How are you {name}?"

akshat_greeting = final_greeting.format(name=name)

print(akshat_greeting)

jose_greeting = final_greeting.format(name="aaaa")

print(jose_greeting)

# x = "Akshat"
# y = input("Enter your name ")

# print(f"Hello {x}, my name is {y}")

ab  =  "33"

print(ab * 12)

num = "3"

num1 = 3

print(num == num1)
print(int(num) == num1)
print(type(num) == type(num1))


"The door is open and the windows are closed"

result = num1 > 1 and num1 < 4

print(result)

res = True

cmp = res and 18

print(cmp)

obj = object()

print(dir(obj))

# print(id([1,2,3]))

# print((42).__class__)
# print(42.__class__)

j= 54
print(id(j))
j=3.8
print(id(j))
print(j.__class__)

print(issubclass(bool,int))

tup = ([1,2,3,4,4,5],"mudit","parakh")
print(tup)
tup[0][1] = 11

print(tup)

tup[0] = "aaaaa"