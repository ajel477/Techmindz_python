# whollow square
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i == 1 or i == 5 or j == 1 or j==5:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# # I shape pattern

# for i in range(1,8):
#     for j in range(1, 8):
#         if i == 1 or i == 7 or j == 4:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# H shape pattern

# for i in range(1, 8):
#     for j in range(1, 8):
#         if j == 1 or j == 7 or i == 4:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# S shape pattern

for i in range(1, 8):
    for j in range(1, 8):
        if i == 1 or i == 4 or i == 7 or (i == 2 and j == 1) or (i == 3 and j == 1) or (i == 4 and j == 1) or (i == 5 and j == 7 ) or (i == 6 and j == 7 ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 