# exceptions
# events that affect the execution of our program

# errors (already pre-defined classes in python)
# syntax error
# type error
# name error
# indentation error

# a = 5
# b = 0
# print(a/b)     # gives ZeroDivisionError
# print("mohan") # line wont execute

# In order to continue the execution of the program even after getting errors, we use the the concept of exception handling 


# try: # place the particular code in try block where their is a chance of getting an error
#     a = 5
#     b = 0
#     print(a/b) #Zero division error
# except Exception as e: # to find the specific error and store it in e
#     print("you have an error", e)
# finally:                            # exectues even if their is no exception or if their is an exception
#     print("Executed")

# print("mohan")


# Handling multiple exceptions
# a = int(input("Enter the number:")) # value error since we gonna give a string instead of integer
# b = "mohan"
# print(a+b) # type error coz int and str addition not possible

# adding try and except block

# try: # try must have atleast one except block
#     a = int(input("Enter the number: "))
#     b = "mohan"
#     print(a+b)
# except ZeroDivisionError:
#     print("you cannot divide a number with 0")
# except ValueError:
#     print("Check the value ")
# except TypeError:
#     print("the operation is invalid")

# print("mohan")

# custom errors

# name = "das"
# if name == "das":
#     raise NameError("name should not be das")


# a = 5
# del(a) # deletes a from memory
# print(a)

# file handling
#read
#write
# text based 

# file1 = open('data.txt', "r") # read
# print(file1)
# print(file1.read())
# file1.close()


# file2 = open("myfile.txt", "w") # creates a new txt file automatically 
# file2.write("this month is july, 13, 2004") #overwrites the data if any
# print(file2) # if we want to read the myfile.txt then we have to open it first and then use the read()
# file2.close()

# # instead of overwriting the existing file content we can add data to the existing file content
# file3 = open("myfile.txt", "a") # appends data to existing file
# #file3.write("\nwe are here")
# for i in range(1,101):
#     file3.write(f"\nless go {i}")
# file3.close()

# os 

import os
# os.mkdir("images") # creates new folder
# os.remove("data.txt") # removes the file
# os.rename("myfile.txt", "demo.txt") # renames the file

# to check if a file exists in a certain path

pat = "D:\\Major Project demo"
if os.path.exists(pat):
    print("path exists")
    if os.path.isfile(pat): # check if its a file 
        print("this is a file")
    elif os.path.isdir(pat): # check if its a folder
        print("this is a folder")