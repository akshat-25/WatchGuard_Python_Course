import time
import random
from threading import Thread


counter = 0

def increment_conuter():
    global counter
    counter += 1
    print(f'New counter value : {counter}')
    print('--------')
    
for x in range(10):
    t = Thread(target=increment_conuter) 
    t.start()