# def greet():
#      name = input("Enter your name ")
#      print(f"Hello, {name}")
     
# greet()
# Arguement -> value you pass in to the function
# Parameter -> variable that accepts a value inside the function 



def calculate_mpg(car_to_calculate):
    mpg = car_to_calculate["mileage"]/ car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f"{name} does {mpg} miles per gallon.")

calculate_mpg({ 
    "make": "Maruti",
    "model": "Swift",
    "mileage": 23000,
    "fuel_consumed": 460
})


print(1,2,3,4,5, sep=" - ")
