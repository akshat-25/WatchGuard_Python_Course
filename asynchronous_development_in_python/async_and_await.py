from collections import deque
from types import coroutine

friends = deque(('a','b','c','d'))

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')
        
async def greet(g):
    print('starting....')
    await g
    print('ending....')
    
        
        
greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Hello world multitasking')
greeter.send('How are you, ')
greeter.send('How are you, ')
