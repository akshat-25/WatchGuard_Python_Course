# Sets don't hold order and they do not contain duplicate elements. 

science_friends = {"Akshat", "qxyz"}
commerce_friends = {"qxyz","abcd"}

print(science_friends)

science_friends.add("Mudit")

print(science_friends)

science_but_not_commerce = science_friends.difference(commerce_friends)

print(science_but_not_commerce)

commerece_but_not_science = commerce_friends.difference(science_friends)

print(commerece_but_not_science)

not_in_both = science_friends.symmetric_difference(commerce_friends)

print(not_in_both)

in_both = science_friends.intersection(commerce_friends)

print(in_both)