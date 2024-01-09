import json

with open('friends_json.txt','r') as file:
    file_contents = json.load(file)
    
print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Discovery'}
]

  
with open('files_project/cars_json.txt','w') as file:
    json.dump(cars,file)

my_json_string = '[{"name": "Kia Seltos", "released" : 2019}]'
new_car = json.loads(my_json_string)  # convert JSON String into a dictionary
print(new_car[0]['name']) 