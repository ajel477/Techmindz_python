# decorators
#functions that enhances other functions
# *args **kwargs


# def saymyname(fun):
#     def wrapper():
#         print("Chamber")
#         fun()
#         print("HeadHunter")
#     return wrapper

# @saymyname
# def hello():
#     print("KillJoy")

# hello()

# # *args, **kwargs

# #positional arguments
# def add(*args):
#     return args

# print(add(5,6,8,4,3,6,7,8,9,))

# # keyword arguments

# def fullname(**args, **kwargs):
#     print(kwargs)

#fullname(fname="robert, lname="dy)

# time module

import time
print(time.time()) # seconds passed since 1970 (unix epoch)
print(time.ctime()) # returns the current local date and time as a human-readable string.

start = time.time()
for i in range(1,11):
    print(i)
    time.sleep(i)
stop = time.time()

print("total execution time:", stop-start)

