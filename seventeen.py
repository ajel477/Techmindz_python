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

# constructor
# used to initialize an object
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
# sum_of_marks()
# average_of_marks()
# display()

# class Student:
#     def __init__( self, n, m1, m2, m3, m4, m5):
#         self.name = n
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#         self.m4 = m4
#         self.m5 = m5

#     def sum_of_marks(self):
#        return self.m1+self.m2+self.m3+self.m4+self.m5

#     def average_of_marks(self):
#         return self.sum_of_marks()/5  # whooof!

#     def display(self):
#         print(f"{self.name} has got total of {self.sum_of_marks()} with an average of {self.average_of_marks()}")

# s1 = Student("sivs", 46,47,44,48,50)
# s2 = Student("pankaj", 34,67,45,68,89)
# s1.display()
# s2.display()


# Inheritance
# single level
#multi level
# mutiple inheritance

# single level inheritance

# class Person1: # Parent class

#     def __init__(self):
#         pass
#     def walk(self):
#         print("I can walk")
#     def smile(self):
#         print("I can smile")
#     def speak(self):
#         print("person1 can speak")

# class Person2(Person1): # child class  single level

#     def __init__(self):
#         pass
#     def dance(self):
#         print("I can dance")
#     def read(self):
#         print("I can read")
#     def speak(self):
#         print("person2 can speak")

# class Person3(Person2): # child class  multi level

#     def __init__(self):
#         pass
#     def sing(self):
#         print("I can dance")
#     def write(self):
#         print("I can read")
#     def speak(self):
#         print("person3 can speak")

# class Person4(Person3, Person2, Person1): # multiple level

#     def __init__(self):
#         pass
#     def sing(self):
#         print("I can dance")
#     def write(self):
#         print("I can read")
#     def speak(self):
#         print("person4 can speak")
#         super().speak()               # calls the method of the immediate super class of Person4

# p2 = Person2()
# p2.smile()  #p2 object inheritnace features from person1 class
# p2.walk()

# p4 = Person4()
# p4.speak() # method overriding child class method will have the priority

# Polymorphism
# poly - many
#morphs - forms

# operator overloading
# class Student:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#     def __add__(self, otr):
#        return self.m1+self.m2, otr.m1+otr.m2   
#     def __sub__(self, rtr):
#         return self.m1-rtr.m1, self.m1-rtr.m2
    
#__sub__
#__mul__
#__truediv__
    
# s1 = Student(7, 8)
# s2 = Student(6, 10)
# print(s1+s2)
# print(s1-s2)

### method overloading
class ABCD:
    def __init__(self):
        pass
    def xyz(self, a):
        print(a)
    def xyz(self, a,b):
        print(a,b)
    def xyz(self, a,b,c):
        print(a,b,c)

a = ABCD()
a.xyz(5)
a.xyz(6,7)
a.xyz(8,9,9)

# method overloading not possible not possible in python because thelast method takes 3 argumemnts and python considers only the last method

# ### method overriding

# class A:
#     def __init__(self):
#         pass
#     def hello(self):
#         print("A hello")
    
# class B(A):
#     def __init__(self):
#         pass
#     def hello(self):
#         print("B hello")

# b = B()
# b.hello()