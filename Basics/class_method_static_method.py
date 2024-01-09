class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)
        
my_object = Foo()
my_object.hi()

class Bar:
    @staticmethod
    def hi():
        print(f"Hello , I am static method")
        
another_object = Bar()
another_object.hi()

class FixedFloat:
    def __init__(self,amount):
        self.amount = amount
    
    def __repr__(self):
        return f"<FixedFloat {self.amount: .2f}>"
    
    @classmethod
    def from_sum(cls,value1,value2):
        return cls(value1+value2)
    
number = FixedFloat(18.2355)
new_number = FixedFloat.from_sum(10.989,34.523)
print(number)

print(new_number)

class Euro(FixedFloat):
    def __init__(self,amount):
        super().__init__(amount)
        self.symbol = 'e'
        
    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount: .2f}>'
    
money = Euro.from_sum(19.2828,93.4648)
print(money)