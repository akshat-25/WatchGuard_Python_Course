from datetime import datetime,timedelta

MAX_LEAVES = 2

def calculate_consecutive_leaves(history):
    print(f'startDate = {start_date}')
    print(f'endDate = {end_date}')
    
    for i in range(0,len(history)-1):
        curr = history[i]
        prev = history[i+1]
        
        if (curr - prev).days == 1:
            return False
               
    return True

def take_casual_leave(start_date,end_date,history):
    number_of_days = (end_date - start_date).days + 1
    
    print(number_of_days)
    
    if number_of_days > MAX_LEAVES:
        return False
    
    consecutive_days = calculate_consecutive_leaves(history)
    
    print(f'WorkingDays = {consecutive_days}')
    
    return consecutive_days
    
history = [
    datetime(2024,1,15),
    datetime(2024,1,5),
  
]

start_date = datetime(2024,1,20)
end_date = datetime(2024,1,20)

result = take_casual_leave(start_date,end_date,history)

print(result)
print(history)