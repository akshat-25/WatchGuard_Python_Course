a = 10
print(id(a))

b = 10

print(id(b))

dict_A = {
    'name' : "Akshat",
    'id' : 10
}

print(id(dict_A))
dict_B = {
    'name' : "Akshat",
    'id' : 10
}

print(id(dict_B))


l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]

print(id(l1))
print(id(l2))


t1 = (1,2)
t2 = (1,2)


print(id(t1))
print(id(t2))