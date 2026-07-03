# import math
# k = [1,2,3,4,5,6,7]

# a = []
# b = []

# middle = math.ceil(len(k) / 2)
# for i in k:
#     if i <= middle :
#         a.append(i)
#     else:
#         b.append(i)
# print(a)
# print(b)


# to print largest and smallest int from list

# a = [2,5,4,8,6,11]

# largest = a[0]
# smallest = a[0]

# for i in a:
#     if i > largest:
#          largest = a[i] 
#     if i < smallest:
#          smallest = a[i]

# print(largest)
# print(smallest) 

# sort the list in ascending order
a = [2,7,8,3,5,9]

# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[j] > a[j+1]:
#             temp = a[j]
#             a[j] = a[j+1]
#             a[j+1] = temp
# print(a)