# string

# sequence of series
# name = 'mohan'
# print(type(name))

# data = "mohan's resume"
# qt = '''gandhi oce said that "say no to violence"'''
# print(qt)

# escape sequence

# \' --'
# \" --"
# \n - new line 
# \n -tab space
# \n -backspace

# data = 'mohan\'s resume'
# print(data)
# qt = 'gandhi\b once\t said \\n that \n \"say no to violence\"'
# print(qt)

#raw string
# qt = r'gandhi\b once\t said \\n that \n \"say no to violence\"'
# print(qt)

# input function
#input() -- considers all inputs as strings defaulty

#type conversion
# a = float(input("enter a number: "))
# b = int(input("enter your second number: "))
# print(a+b)

# c = input("Enter the first word: ")
# d = input("enter the second number: ")
# print(c+' '+d)

#string formatting
name = "ajel"
age = 21
status = False
rating = 4.9

result = rf"My name is {name}, my age is {21}, \n status till now is {status}, and my rating for now is {rating}"
print(result)
