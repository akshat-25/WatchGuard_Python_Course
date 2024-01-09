age = 25 
l1 = [20,25,30]


def increase_age(current_age):
    print(id(current_age) == id(age))
    current_age = current_age + 1
    
print(id(age))
increase_age(age)
print(id(age))

print(age)
print(id(age))



primes = [2,3,5]
print(id(primes))

primes += [7,11]  #primes.__iadd__([7,11])
print("It is id", id(primes))

primes = primes + [2,4,6] #primes.__add__()

print(id(primes))

def set_list(list):
	list = ["A", "B", "C"]
	return list

def add(list):
	list.append("D")
	return list

my_list = ["E"]
print(set_list(my_list))
print(my_list)
print(add(my_list))


e = 12
print(id(e))
e += 13
print(id(e))

