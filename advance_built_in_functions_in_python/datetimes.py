from datetime import datetime,timezone,timedelta

print(datetime.now())
print(datetime.now(timezone.utc)) #2024-01-09 11:20:16.373296+ 00:00

today = datetime.now()
tomorrow = today + timedelta(days=1) #Represent the difference between two datetime objects.

print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M'))

user_date = input("Enter the date in YYYY-mm-dd format: ") # string format time
user_date  =datetime.strptime(user_date, '%Y-%m-%d') # string parse time

print(user_date)