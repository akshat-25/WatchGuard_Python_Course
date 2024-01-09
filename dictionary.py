# Dictionary keep the order 

friend_ages = {
    "Akshat" : 21,
    "Mudit" : 18,
    "Milind" : 21,
}
friend_ages["Harsh"] = 21

print(friend_ages["Akshat"])

print(friend_ages)

friends = (
    {"name" : "Akshat", "Age" : 21},
    {"name" : "Mudit", "Age" : 18},
    {"name" : "Milind", "Age" : 21},
)


print(friends)

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

colors = [("Red",1),("Blue",2),("Green",3)]
colors_dictionary = dict(colors)
print(colors_dictionary)

for age in friend_ages.values():
    print(age)
    
for name,age in friend_ages.items():
    print(f"{name} is {age} years old")