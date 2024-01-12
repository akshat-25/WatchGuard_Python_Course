import time
from threading import Thread

def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello! {user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start}')
    

def complex_calculation():
    print('Started calculating...')
    [x**2 for x in range(20000000)]
    
start  = time.time()
ask_user()
complex_calculation()
print(f'Single thread total time: {time.time() - start}')

thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()
thread1.start()
thread2.start()

# Threads 1 and 2 are running at the same time as our main thread is running

thread1.join()
thread2.join()
# These tells our main thread for method 1 to finish and method 2 ti finish.
# These both are blocking operation

print(f'Two thread total time: {time.time() - start}')


# We should not kill the threads because a deadlock situation may occur.