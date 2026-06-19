# we are back to the basics of python programming
# we will be learning about the basics of python programming

# varables

a = 6
print(id(a))
a = 16
print(id(a))

# swap two numbers

a = 3
b = 7
print("Before swapping: ", a, b)

t = a
a = b
b = t
print("After swapping: ", a, b)

# swapping without temp variable
a = 3
b = 7
print("Before swapping: ", a, b)

a = a + b
b = a - b
a = a - b
print("After swapping: ", a, b)