# functions
#functional programming
# repetitive tasks
#block of code which is executed when it is called

# def name(): #function name
#     print("messi")

# name() # functional calling 

#arguments
#values that are passed to a function

# def add2(a, b):
#     print(a+b)
# add2(3, 6)# actual parameter

# # types of arguments
# #1 positional arguments
def add2(b, a):
    print(a/b)

# add2(3,4)

#2. Keyword arguments
# def leo(x, y, z):
#     print(x + " " + y + " " + z)

# leo(x="ajel", y="mathew", z="varghese")

#3. default arguments

# def funcNam(a=0,b=0):
#     print(a, b)

# funcNam(2, 3)

# return statement
# scope

# def add2(a,b):
#     return a+b #returns the value to the function, nothing will be executed below the return statement
# #if there is more than one item in the return statement it will give a tuple as output


# # to create a calculator using fucntions 

def add(a, b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a, b):
    return a/b

def main():
    while True:
        print("Diabolic Calculator")
        op = int(input("Enter the operation to perform : 1. Add\n 2.Substract\n 3.Multiply\n 4.Divide\n 5.Exit"))
        if op == 5:
            break
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second nunber: "))
        if op == 1:
            print(add(x,y))
        elif op == 2:
            print(sub(x,y))
        elif op == 3:
            print(mul(x,y))
        elif op == 4:
            print(div(x,y))
        else:
            print("Invalid Operation")

main()


# lamda functions
#to write small fucntions in a single line

# z = lamda x,y : x+y

#product of 3 numbers
#square of a number
#perimeter of a circle
#area of triangle

# z = lambda x,y,z : x*y*z

# print(z(2,3,4))

# z = lambda x : x**2
# print(z(2))

# z = lambda radius : 2 * 3.14 * radius
# print(z(4))

# z = lambda base, height : (base*height)/2
# print(z(3,4)) \

#check if a person is eligible or not 
# turnary operator (all in sinlge line)
# only possible for single if else statement

# age = 24

# print("eligible") if age >= 18 else print("not eligible")

# # using lambda function

# age = lambda age : "eligible" if age > 18 else "not eligible"

# print(age(21))

