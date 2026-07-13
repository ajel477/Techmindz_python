#object oriented programming

# what is object ?
# real life entity

#2
# attributes define an object
#behaviours / methods

#class - blueprint
# to create objects

#Object CAR
#its attributes
# name
# model
# color

# methods = functions inside a class
# objects = instance of a class

#creating class car
# class Car:
#     def start():
#         print("the car has started")
#     def stop():
#         print("the car has stopped")
        
# c1 = Car
# c2 = Car
# c3 = Car
# c1.start()
# c1.stop()

# infinite object can be created for the class car

#constructor
#used to initialize an object
# __init__() defined using this method, automatically called whe an object is made

# class Car:
#     def __init__(self):
#         print("the object is initialized") # gets called whenever an object of the class is created 
#     def start(self):
#         print("the car has started")
#     def stop(self):
#         print("the car is stopped")

# c1 = Car()
# c1.start()

#  the attributes essential for the objects can be defined inside the __init__() method. so when an object is created it will get its attributes already defined.
# class Car:
#     def __init__(self):
#         self.name = "porche 911"
#         self.color = "red"
#         print("the object is initialized") 
#     def start(self):
#         print("the car has started")
#     def stop(self):
#         print("the car is stopped")

# c1 = Car() # botht objects c1 and c2 will have the same attributes for now since we hardcoded the attribute values
# c2 = Car()
# print(c1.name)
# print(c1.color)
# print(c2.name)
# print(c2.color)

# __init__() is a magic method since it will get called without calling it

# Now if we want different attributes for diffrerent objects then we have to pass arguments while creating object and get them in out constructor method
# class Car:
#     def __init__(self, n, c): # self is basically used to refer the current object which we are using. in this scenario self will point to object c1 first and then c2 afterwards
#         self.name = n
#         self.color = c
#         print("the object is initialized") 
#     def start(self):
#         print(f"the {self.name} has started")
#     def stop(self):
#         print("the car is stopped")

# c1 = Car("swift", "black") 
# c2 = Car("roll royce", "white")
# print(c1.name)
# print(c2.name)
# c1.start() # self is pointing to object c1 and c1.name = n that is swift
# c2.start() # now self points to c2


# create a class with 6 attributes name, m1, m2, m3, m4, m5

# 3 methods
#sum_of_marks()
#average_of_marks()
#display()

class Student:
    def __init__(self, n, m1, m2, m3, m4, m5):
        self.name = n
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5

    def sum_of_marks(self):
       return self.m1+self.m2+self.m3+self.m4+self.m5

    def average_of_marks(self):
        return self.sum_of_marks()/5  # whooof!

    def display(self):
        print(f"{self.name} has got total of {self.sum_of_marks()} with an average of {self.average_of_marks()}")

s1 = Student("sivs", 46,47,44,48,50)
s1.display()







