# generators
#lazy iterables
#give values on demand

# generator

# def mydata(): # generator object
#     yield "one"
#     yield "two"
#     yield "three"
#     yield "four"

# print(mydata())
# print(list(mydata()))

# a = mydata()
# print(next(a))
# print(next(a))
# print(next(a))

# import sys


#map
# maps each item in an iterable to a function
# map(func, iterable)

# def square(z):
#     return z**2

# z = lambda x : x**2

# a = [1,2,3,4,5,6,7,8]

# result = map(z,a)
# print(list(result))

z = lambda x : x**2

products = [
    ("nike", 123),
    ("apple", 423),
    ("samsung", 444),
    ("ps5", 2322),
    ("iphone", 3423)
]

def toINR(z):
    return z[1]*96.34


#filter

