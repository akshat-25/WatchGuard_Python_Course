import time
from concurrent.futures import ProcessPoolExecutor

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


start = time.time()

with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)
    

print(f'Two process total time:{time.time() - start}')