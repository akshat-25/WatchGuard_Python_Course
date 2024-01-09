cars = ["ok1","ok2","ok3","faulty","ok4","ok5"]

for status in cars:
    if status == "faulty":
        print("Stopping the pipeline")
        break
    print(f"This car is {status}")
else:
    print("All cars are ok")  


for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} is Not prime")
            break
    else:
        print(f"{n} is a prime number")
        
print(cars[:]) # Here we are building a new list.

print(cars[-3:]) #It start counting from 3 element from ending to end