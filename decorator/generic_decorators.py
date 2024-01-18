# A decorator is just a function that returns another function
import functools
user = {'username': 'akshat123', 'access_level': 'admin'}

def user_has_permission(func):
   @functools.wraps(func)
   def secure_func(*args, **kwargs):  # It is a kind of wrapper function around the func
       if user.get('access_level') == 'admin':
           return func(*args, **kwargs)
   return secure_func
   

@user_has_permission
def my_function(panel):
    """
    Allow us to retrieve he password for the admin panel
    """
    return f'Password for {panel} panel is 12345'

@user_has_permission
def another_func():
    pass

print(my_function('movies'))
# print(my_function.__name__)
# print(my_function.__doc__)
# print(another_func.__name__)

# another_func('movies')

