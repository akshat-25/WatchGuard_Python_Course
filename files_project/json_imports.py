import json

file = open('files_project/friends_json.txt','r')
file_contents = json.load(file) # reads file and turns it into a dictionary

file.close()

print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Discovery'}
]

  
file = open('files_project/cars_json.txt','w')
json.dump(cars,file)
file.close()

my_json_string = '[{"name": "Kia Seltos", "released" : 2019}]'
new_car = json.loads(my_json_string)  # convert JSON String into a dictionary
print(new_car[0]['name'])


