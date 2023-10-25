def checker(list_of_numbers, number):
    if number in list_of_numbers:
        return True
    else:
        return False


user_input = [1, 2, 3, 4, ]
user_check = 8
print(checker(user_input, user_check))
