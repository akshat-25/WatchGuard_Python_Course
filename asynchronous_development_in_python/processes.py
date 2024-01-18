import time
from multiprocessing import Process


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



process = Process(target=complex_calculation)
process2 = Process(target=ask_user)
process.start()

start = time.time()

ask_user()

process.join()
process2.join()

print(f'Two process total time:{time.time() - start}')