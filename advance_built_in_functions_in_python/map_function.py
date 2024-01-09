friends = ['Akshat','Ayush','Harsh','Miling','Shreyansh']

friends_lower = map(lambda friend: friend.lower(), friends)
friends_lower = (friend.lower() for friend in friends)

print(next(friends_lower))


class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    @classmethod
    def from_dict(cls,data):
        return cls(data['username'],data['password'])
    
users = [
    {'username' :'Akshat','password' : '123'},
    {'username' :'Mudit','password' : '321'},
    {'username' :'Parakh','password' : '124'},
]

users = map(User.from_dict,users)