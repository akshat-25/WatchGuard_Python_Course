friends = input("Enter 3 friends name").split(',')

people = open("files_project/people.txt","r")

people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)

people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('files_project/nearby_friends.txt','w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')

nearby_friends_file.close()


print("Helloooooo")

