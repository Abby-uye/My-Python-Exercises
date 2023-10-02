# for number in range(11):
#     print("* ")
#     for index in range(1, number):
#         print("* ", end='')
# for index2 in range(11 -1):
#     print(" ",end='')
#     for index in range(index2 -1):
#         print(" ", end=' ')
# for column in range (11, 1):
#     print("* ")
#     for row in range(column):
#          print("* ", end='')

for number in range(1, 11):
    for row1 in range(number):
        print("*", end=" ")

    for row2 in range(number, 11 - 1):
        print(" ", end=" ")

    for row1 in range(number):
        print(" ", end=" ")

    for row2 in range(number, 11 - 1):
        print("*", end=" ")
    print()
    for row1 in range(number):
        print(" ", end=" ")

    for row2 in range(number, 11 - 1):
        print(" ", end=" ")
    for row3 in range(number,11,-1):
        print("*",end=" ")
    print()