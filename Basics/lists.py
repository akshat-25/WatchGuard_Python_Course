# We should keep Homogeneous Data inside a list.

friends = ["Akshat","Harsh","Milind","Ayush"]

print(friends)
print(friends[0])
print(len(friends))

friends_and_ages = [["Akshat",22],["Harsh",21],["Milind",21],["Ayush",21]]

print(friends_and_ages)

print(friends_and_ages[0][1])

friends.append("Navpreet")

print(friends)
print(len(friends))

friends_and_ages.remove(friends_and_ages[3])
print(friends_and_ages)
