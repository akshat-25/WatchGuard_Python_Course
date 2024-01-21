def printer(*args,**kwargs):
    print(type(args))
    for item in args:
        print(item)
    
    print(type(kwargs))
    for key,value in kwargs:
        print("Hi")
        print(key,value)
       

l1 = ['a','b','c','d','e','f']

d1 = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4
}

printer(l1,d1)