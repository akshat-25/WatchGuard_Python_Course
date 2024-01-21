
def decor(division):
    def inner(*args):
        for num in args[1:]:
            if num == 0:
                return "Cannot divide by zero"
        return division(*args)
    return inner
        

@decor
def div1(a,b):
    return a/b

@decor
def div2(a,b,c):
    return a/b/c


print(div1(2,0))
print(div2(4,6,0))
