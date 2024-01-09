def starts_with_a(friend):
    return friend.startswith('A')

friends = ['Akshat','Ayush','Harsh','Mi__ling','Shreyansh']

# start_with_a = filter(lambda friend: friend.startswith('M'), friends) #arg 1: function that return True/False

# print(list(start_with_a))
# print(list(start_with_a))

start_with_r = my_custom_filter(lambda friend: friend.startswith('A'),friends)

another_starts_with_r = (f for f in friends if f.startswith('A'))

def my_custom_filter(func,iterable):
    for i in iterable:
        if func(i):
            yield i