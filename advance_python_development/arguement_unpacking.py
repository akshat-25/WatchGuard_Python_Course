accounts = {
    'current' : 1000.00,
    'savings' : 1500.00
}

def add_balance(amount: float, name: str) -> float:
    accounts[name] += amount
    return accounts[name]


transactions = [
    (-100.50,'current'),
    (-200.50,'savings'),
    (-300.50,'current'),
    (400.50,'savings'),
    (500.50,'current'),
    (600.50,'savings'),
    (700.50,'current'),
]

for t in transactions: 
    # add_balance(*t)  # This unpacks the iterable to the arguements of the function
    add_balance(name=t[1],amount=t[0]) # Named Arguements
    
class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    @classmethod
    def from_dict(cls,data):
        return cls(data['username'], data['password'])
    

users = [
    {'username': 'Akshat', 'password': 'Akshat123'},
    {'username': 'Parakh', 'password': 'Parakh123'},   
]

# user_objects = map(User.from_dict,users)
# user_objects = [User.from_dict(u) for u in users ]
# user_objects = [User( data['username'],data['password']) for data in users]

user_objects = [User(**data) for data in users]

