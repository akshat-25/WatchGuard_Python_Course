
def decor1(get_name):
    def to_upper():
        lower = get_name()
        return lower.upper()
    return to_upper

def decor2(get_name):
    def to_list():
        return get_name().split()
    return to_list
    
@decor2
@decor1
def get_name():
    name = input("Enter first name: ")
    surname = input("Enter last name: ")
    fullname = name +" " + surname
    return fullname

print(get_name())



#decor1 = AKSHAT PARAKH
#decor2 = ['AKSHAT','PARAKH']