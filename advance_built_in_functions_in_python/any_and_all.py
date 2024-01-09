friends = [
    {
        'name' : 'Akshat',
        'location': 'Noida,UP'
    },
    {
        'name' : 'Mudit',
        'location': 'Bhopal,MP'
    },
    {
        'name' : 'Harsh',
        'location': 'Jaipur,RJ'
    },
    {
        'name' : 'Miling',
        'location': 'Bikaner,RJ'
    },
]

your_location = input('Where are you right now?')
friends_nearby = [friend for friend in friends if friend['location'] == your_location]
if any(friends_nearby): #True if there's at least one,; or False if empty
    print('You are not alone!')
    
    
"""
* 0,0.0
* None
* [],(),{}
* False
"""

print(bool(0))