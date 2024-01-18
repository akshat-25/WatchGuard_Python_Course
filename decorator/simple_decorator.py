# A decorator is just a function that returns another function
import functools
user = {'username': 'akshat123', 'access_level': 'admin'}

# third level returns a function that takes in a function
def third_level(access_level):
    def user_has_permission(func):
        @functools.wraps(func)
        def secure_func(panel):  # It is a kind of wrapper function around the func
            if user.get('access_level') == access_level:
                return func(panel)
        return secure_func 
    return user_has_permission

@third_level('admin')
def my_function(panel):
    """
    Allow us to retrieve he password for the admin panel
    """
    return f'Password for {panel} panel is 12345'

# @user_has_permission
# def another_func():
#     return 'Hello'

# print(my_function('movies'))
# print(my_function.__name__)
# print(my_function.__doc__)
# print(another_func.__name__)

# another_func('movies')

user_has_permission = third_level('admin')
my_function = user_has_permission(my_function)
print(user_has_permission)