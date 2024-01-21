
def decor(printer):
    def inner():
        printer()
        print("Welcome!!")
    return inner

@decor
def printer():
    print('Welcome!!')
    print('Welcome!!')
    
# printer()
# printer = decor(printer)
printer()
