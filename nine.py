# list 
# collection of data 

a = [2,4,1,5,3,1,3,5,2,4,5,2,6,2]

# properties of lists

#lists can have any element of any size

data = [1,2.3, "mohan"]

# lists are ordered
# a = [1,2,3,4]
# b = [4,3,2,1]

# print(a == b)

# lists are indexed

a = [11,12,13,14,15,16]
# print(a)
# print(a[3])
# print(a[2:5])
# print(a[::-1])

#     #012345678   
# b = "mohan das"
#          -2,-1   

# lists are mutable (means the values inside lists can by changed or modified)
# but strings are immutable

# a = [11,12,13,14,15]
# a[0] = 'mohan'
# print(a)

# lists are dynamic because they are mutable

# lista are nested

# a = [11,12,[100,300],14,15]
# print(a[2][0])

# or 

# b = a[2]
# print(b[0])

# inbuilt methods

#to add elements

#.append() -- adds element to the end of the list
# a = [11,12,13,14]
# a.append(16)
# print(a)
# #.extend() -- adds an iterable or a mini list to the list
# a = [11,12,13,14]
# a.extend([56,78,"mohan"])
# print(a)


#.insert() -- adds elements to specific index\
# a = [11,12,13,14,11]
# a.insert(0, "mohan")
# print(a)

#to remove elements
#.remove()
# a = [11,12,13,14,15]
# a.remove(11)
# print(a)

#.pop()

# a = [11,12,13,14,32,45,56,11,11]
# a.pop(0) # removes only the last element
# a.pop(1) #removes element at the specified index
# print(a)

# tuple
# collection of data
# a = (2,3,1,"mohan",734)
# print(a[::-1])

# ordered and indexed same like lists only difference is tuple is immutable

#iterable
#str, list, tuple, set, dict
#index based and direct looping iterable are str, list, tuple

#direct looping
#for i in a:
#    print(i)

#index based looping
a = ["apple", "orange", "banana", "pineapple", "mango"]

for i in range(5):
    print(i, a[i])