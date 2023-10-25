# def biggest_odd(numbers):
#     maxed = 0
#     for item in numbers:
#         the_number = int(item)
#         if the_number % 2 != 0:
#             if the_number > maxed:
#                 maxed = the_number
#     return maxed
#
# print(biggest_odd("29867"))

# def bigger_odd(numbers):
#     return max([numbers for number in numbers if int(number)])
#     return filter(lambda n:int(n) % 2==1,numbers)
# print(bigger_odd("35462"))
test_list = [[0, 0, 0],
             [0, 0, 0]]
for i, val in enumerate(test_list):
    for j,number in enumerate(val):
        test_list[i][j] = 5

print(test_list)
