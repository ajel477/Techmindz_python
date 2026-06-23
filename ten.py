#set
#collection of data
# --  set is unordered and no index, index based looping not possble
# -- contains no duplicate elements

# a = {1,2,3,4}
# b = {4,3,2,1}

# print(a == b)

fruits = {"chakka", "thenga", "manga", "pazham"}
vegs   = {"cucumber", "tomato"}

for i in fruits:
    for j in vegs:
        print(i+ " " + j)

# set is mutable
#union
#intersection

a = {1,2,3,4,5}
b = {5,6,7,8}

print(a.union(b))
print(a|b)
print(a.intersection(b))
print(a&b)
print(a-b)
print(b-a)

#dictionary
#key value paired datatype
# no index
#mutable and dynamic

userdata = {"name": "mohan", "age": 22, "location":"kochi"}
userdata["status"] = 9

print(type(userdata))
print(userdata)

#restrictions in ditionary

# 1. Keys are unique
# 2. keys are immutable type


#inbuilt functions

# get() gets value of the certain key
# keys() to get all keys
# values() to get all values
# items() list of key value pairs
# update() updates the key value pair, if not present then create new pair
# pop() removes the key and its associated value
# popitem() removes last key and its value
# clear() all gets removed

userdata = {"name": "mohan", "age": 22, "location":"kochi"}

for i,j in userdata.items():
    print(i, j])



