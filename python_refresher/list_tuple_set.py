l = ['akshat','mudit']
print(l)

l += 'parakh'
l.append('Bhilwara')

print(l)

country = {"India","Russia","Germany"}
cou = {"Australia","Nepal","India"}

ans = country.difference(cou) # country - cou
print(type(ans))
print(ans)


print(country.union(cou))

both = country.intersection(cou)
print(both)

l1 = ['a','b']
s1 = {'a','b'}

print(l1 == s1)
print(l1 is s1)