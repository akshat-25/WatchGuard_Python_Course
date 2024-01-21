def decor(addition):
    def add():
        sum1 = addition()
        num3 = float(input("Enter 3rd number: "))
        sum = sum1 + num3
        return sum
    return add

# @decor
def addition():
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    sum = num1 + num2
    return sum

addi = decor(addition)
print(addi())
# print(addition())
