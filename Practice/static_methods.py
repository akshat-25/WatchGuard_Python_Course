class A:
    b = 5
    def __init__(self):
        self.a = 10
      
    def get(self):
        print(self.a)
        
          
obj = A()
print(obj.a)

obj.a = 11

print(obj.a)

obj.get()

print(A.b)

print(obj.b)

A.b = 55

print(A.b)

obj.b = 123

print(obj.b)

print(A.b)


