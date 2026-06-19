# for loop 

# for i in range(start, stop, step):
#     logic writtne here

# sum of 100 numbers using while loop 

# num = int(input("Enter the number: "))

# sum = 0

# for i in range(1,101,1):
#     sum = sum + i

# print(sum)

#factorial of a number 

# num = int(input("Enter the number: "))

# factorial = 1

# for i in range(num,1,-1):
#     factorial = factorial * num
#     num = num - 1

# print(factorial)

#multiplication table of a number

# num = int(input("enter the number: "))

# for i in range(1,11,1):
#     print(f'{num} X {i} = {num*i}')


#sum and average of n numbers 

count_of_numbers = int(input("Enter the count: "))
sum = 0
for i in range(count_of_numbers):
    num = int(input("Enter number: "))
    sum = sum + num
print(f'sum is {sum}')
print(f'the average is {sum/count_of_numbers}')


