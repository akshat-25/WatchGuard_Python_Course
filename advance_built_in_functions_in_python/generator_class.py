class FirstHundredGenerator:
    def __init__(self):
        self.number = 0
        
    def __next__(self): #next(my_object)
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

class FirstHundredIterator():
    def __iter__(self):
        return FirstHundredGenerator()

print(sum(FirstHundredIterator()))

for i in FirstHundredIterator():
    print(i)
