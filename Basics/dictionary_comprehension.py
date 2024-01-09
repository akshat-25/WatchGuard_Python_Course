friends = {"Akshat","Mudit","Parakh"}
time_since_seen = {3,7,4}

# long_timers = {
#     friends[i]: time_since_seen[i]
    
#     for i in range(len(friends))
#     if time_since_seen[i] > 4
# }

long_timers = dict(zip(friends,time_since_seen))
print(long_timers)  
