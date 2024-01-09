file = open("files_project/csv_data.txt")
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]
print(lines)
for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()
    print(f'{name} is {age}, studying {degree} at {university}')

    
sample_csv_value = ', '.join(['Navi','21','Chitkara','BTech'])
print(sample_csv_value)