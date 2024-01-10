def hundred_numbers():
    nums=[]
    i=0
    while i<100:
        yield i # By using yield we are making generator and it turns this into a python object
        
        i += 1

print(hundred_numbers())

# print([x * 2 for x in hundred_numbers()])

g = hundred_numbers()
print(next(g))
print(next(g))

my_range_obj = range(10)
print(my_range_obj)

list(g)