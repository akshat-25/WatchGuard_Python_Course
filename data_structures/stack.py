class Stack:
    def __init__(self):
        self.items = []
        
    def push(self,e):
        self.items = [e] + self.items
        
    def pop(self):
        return self.items.pop()
    
    
s = Stack()
s.push(5)  # [5]
s.push(10) # [10,5]
s.push(15) # [15,10,5]

print(s.pop())

print(s.items)