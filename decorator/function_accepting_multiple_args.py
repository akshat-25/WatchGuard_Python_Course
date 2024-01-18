# def add_all(a1,a2,a3,a4):
#     return a1+a2+a3+a4

# with single asterisk args, we can accept any number of positional arguements.
def add_all(*args):
    return sum(args)
    print(args)

# vals = {'a1' : 1, 'a2': 3, 'a3': 5, 'a4': 7}
vals = (1,2,3,4)
print(add_all(*vals))

#  with double asterisk args,we can accept any number of named arguements.
def pretty_print(**kwargs):
    for k, v in kwargs.items():
        print(f'For {k} we have {v}.')
        

pretty_print(**{'username' : 'akshat123', 'access_level': 'admin'})