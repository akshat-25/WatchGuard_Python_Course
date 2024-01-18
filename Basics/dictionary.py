# Type of collection
# Mutable in nature
# Dynamic in nature. Can grow and shrink as needed.
# Dictionary keep the order
 
friend_ages = {
    "Akshat" : 21,
    "Mudit" : 18,
    "Milind" : 21,
    "ages": [1,2,3,4,5,6,7,8,9],
    "set" : {"akshat","parakh"},
    "nested-dict": {
        "key1": 1,
        "key2": 2
    }
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
    
    
print(friend_ages)

cricket_team = dict([
    ('captain', 'Virat Kolhi'),
    ('Keeper', 'KL Rahul')
])

cricket_team2 = dict(
    Captain = 'Virat',
    Keeper = 'KL',
    Dhoni = 7,
)


print(cricket_team)
print(cricket_team2)

del cricket_team["Keeper"]

print(cricket_team)

print(cricket_team['captain'])


dictionary_cls = {} 

print(type(dictionary_cls))

