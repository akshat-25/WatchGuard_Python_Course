def smart_divider(func):
    def inner(num1,num2):
        if num2 == 0:
            print('Cannot divide by 0')
            return
        func(num1,num2)
    return inner

@smart_divider
def division(num1,num2):
    print("Division is: ",num1/num2)


# Division = smart_divider(division)
# Division(10,2)

division(10,0)
