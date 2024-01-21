import functools

# The @functools.wraps decorator uses the function functools.update_wrapper() to update special attributes like __name__ and __doc__ that are used in the introspection.

def do_twice(func):
    @functools.wraps(func) # Used to preserve the identity of the function using the decorator.
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return wrapper
        
@do_twice
def say_hello():
    print('Hello!!')

@do_twice    
def greet(name):
    print(f'Hello {name}')
    return 'I\'m the return value'

say_hello()
return_value = greet('Akshat')
print(return_value)

print(say_hello.__name__)
print(say_hello)