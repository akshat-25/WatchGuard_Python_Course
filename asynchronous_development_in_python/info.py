# We cannot run 2 threads in one process at the same time
# Each process in python creates a key resource
# When a threas is running, it must acquire that resource
# Since there is only one of that, only one thread can run in a process at once.

# GIL -> Global Interpreter Lock

