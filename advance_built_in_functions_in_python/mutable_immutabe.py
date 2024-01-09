friends = {
    'akshat' : 1,
    'milind' : 2,
    'harsh' : 3,
    'ayush' : 4
}


def friends_fun(friends_dict,name):
    print(id(friends_dict))
    friends_dict[name] = 0
    
    
print(id(friends)) 
# friends_fun(friends,"akshat")
# print(id(friends))

print(id(friends["akshat"]))
friends_fun(friends,"akshat")
print(id(friends["akshat"]))
print(id(friends)) 

