# the_list = [15,6,7]
# for index in range(len(the_list)):
#     print(the_list)
# for index in the_list:
#     print(the_list)

credit_card_number = [4, 3, 8, 8, 5, 7, 6, 0, 1, 8, 4, 0, 2, 6, 2, 6]
position = 0
for index, value in enumerate(credit_card_number):
     if index % 2 == 0:
    #     value = credit_card_number[index] * 2
    #     if value > 9:
    #         the_modulo = int(value % 2)
    #         result = int(value / 2)
    #         position += int(the_modulo + result)
    #     else:
    #         position += int(value)
        print(f"{index}, {value}")
    # print(position)
