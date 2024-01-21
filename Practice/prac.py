my_dict = {
'a' : 1,
'b' : 2
    
}


my_dict['c'] = 3


sum = 0

for key,value in my_dict.items():
    sum += my_dict[key]
    
print(sum)

my_dict = dict((key,value) for key,value in my_dict.items() if value<=1)

print(my_dict)