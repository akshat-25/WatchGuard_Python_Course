numbers = [0,1,2,3,4,5]
double_numbers = []

for number in numbers:
    double_numbers.append(number*2)
    
print(double_numbers)

triple_numbers = [number * 3 for number in numbers]

print(triple_numbers)

four_times_numbers = [_ * 4 for _ in range(6)]
print(four_times_numbers)

friends_ages = [22,31,45,24]

age_string = [f"My friend is {age} years old." for age in friends_ages]
print(age_string)

names = ["Akshat", "Mudit"]

lower = [name.lower() for name in names]

print(lower)