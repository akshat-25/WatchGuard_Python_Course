class Queue:
    def __init__(self):
        self.items = []
        
    def push(self,e):
        self.items.append(e)
        
    def pop(self):
        head = self.items[0]
        self.items = self.items[1:]
        return head
    
q = Queue()
q.push(5)  
q.push(10)
q.push(15)

print(q.items)

print(q.pop())
print(q.pop())