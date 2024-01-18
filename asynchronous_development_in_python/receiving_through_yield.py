from collections import deque

friends = deque(('a','b','c','d'))

def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')
        
def greet(g):
    yield from g
    # g.send(None)
    # while True:
    #     greeting = yield
    #     g.send(greeting)
        
        
greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Hello world multitasking')
greeter.send('How are you, ')