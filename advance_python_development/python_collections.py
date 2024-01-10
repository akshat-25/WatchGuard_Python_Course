"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""

from collections import Counter,defaultdict,OrderedDict,namedtuple,deque

temp = [13.5,56.7,765.3]

temp_counter = Counter(temp)
print(temp_counter[56.7])

print(Counter({'hello' :5,'hi' : 4})['hi'])

friends = [('Akshat','SKIT'),('Ayush','SKIT'),('Akshat','Sangam')]

# alma_maters = {}

# for friend,place in friends:
#     if friend not in friends:
#         alma_maters[friend] = []
        
#     alma_maters[friend].append(place)
    
    
# print(alma_maters)

alma_maters = defaultdict(list)

for friend,place in friends:
    alma_maters[friend].append(place)

alma_maters.default_factory = None # We'll get a keyerror in the case if the key does not exist by using this default_factory = None
    
print(alma_maters)


my_comapany = 'FoodWorks'

coworkers = ['Akshat','Harsh','Miling','Ayush']
other_coworkers = [('Shreyansh','SKIT'),('Harshil','SKIT'),('Vaibhav','Sangam')]

coworker_companies = defaultdict(lambda: my_comapany) # defaultdict takes in a function

for person, company in other_coworkers:
    coworker_companies[person] = company
    
print(coworker_companies[coworkers[0]])
print(coworker_companies['Navpreet'])

# OrderedDict

o = OrderedDict()
o['Akshat'] = 5
o['Ayush'] = 9
o['Milind'] = 10
o['Harsh'] = 54
print(o)
o.move_to_end('Akshat')
print(o)
o.move_to_end('Harsh',last=False)
print(o)


# namedtuple

account = ('Current',30000)

Account = namedtuple('Account', ['name','balance'])

account = Account('savings',2000.50)

print(account)

accountNamedTuple = Account(*account)

print(accountNamedTuple._asdict()['balance'])


# deque -> It is thread safe

friends = deque(('Akshat','Navpreet','Ayush','Harsh','Milind'))

friends.appendleft('Shreyansh')

print(friends)

friends.rotate

friends.insert