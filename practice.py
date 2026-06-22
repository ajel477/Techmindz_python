# lia = [12,13,14,40,16,17]

#to find the mean of the give list elements
# sum = 0

# for i in range(len(lia)):
#     sum = sum + lia[i]

# mean = sum/len(lia)

# print(mean)

# to find the greatest element and print its index

# largest = lia[0]

# for i in range(len(lia)):
#     if lia[i] > largest:
#         largest = lia[i]
#         index = i

# print(f"the largest number is  {largest} and its index is  {index} ok")

# dictionaries

# d1 = {1:100, 2:200, 3:300, 4:400}
# d2 = {5:500, 6:600, 7:700, 8:800}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)


#two numbers adding up to a target sum
# target = int(input("Enter the target number: "))
# input = [2,7,11,15]

# for i in range(len(input)-1):
#     if target == input[i] + input[i+1]:

#      print(i, i+1)


#rotate an array to k steps in place

# arr = [1,2,3,4,5]
# k = 2

# while k > 0:
#     temp = arr[-1]
#     for j in range(len(arr)-1,0,-1):
#         arr[j] = arr[j-1]
#     arr[0]  = temp
#     k = k-1

# print(arr)

# palindrome check
# a = "madam"

# b = ""

# for i in range(len(a)-1, -1, -1):
#     b = b + a[i]

# if a == b:
#     print("yes")
# else:
#     print("No")

#move all zeroes to the end in an array

# arr = [0,1,0,3,12]

# j = 0

# for i in range(len(arr)):
#     if arr[i] != 0:
#        temp = arr[i]
#        arr[i] = arr[j]
#        arr[j] = temp
#        j = j + 1

# print(arr)

#to find the first non_repeating character in a string

# a = "aabbbcdde"

# d1 = {}

# for i in a:
#     if i in d1.keys():
#         d1[i] = d1[i] + 1
#     else:
#         d1[i] = 1

# for i in a:
#     if d1[i] == 1:
#         print(f"the first non-repeating character is {i}")
#         break

# print(d1)

#program to sum all values in a dictionary

# d1 = {1:10, 2:20, 3:30}

# sum = 0

# for i in d1:
#     sum = sum + d1[i]

# print(sum)

# prime number check

# num = int(input("Enter the number: "))

# is_Prime = True

# if num <= 1: 
#     is_Prime = False
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             is_Prime = False
#             break

# if is_Prime:
#     print("This is a prime number!")
# else:
#     print("This is not a prime number")

    