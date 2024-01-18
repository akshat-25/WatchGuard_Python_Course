# What ?
# Single line smart statements provided by python to create list

# Syntax
#l1 = [expression for e in sequence]


list1 = [2*e for e in range(1,11)]

print(list1)


list2 = [11,12,132,3473,373,585,82,694,89]

l1 = [e for e in list2 if e%2 is 0]

print(l1)