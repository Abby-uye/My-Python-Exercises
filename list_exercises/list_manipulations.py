def list_of_numbers(list_ofNumbers):
    return list_ofNumbers


def list_of_odd_numbers(list_to_test):
    odd_numbers = []
    numbers = 0
    for numbers in list_to_test:
        if numbers % 2 != 0:
            odd_numbers.append(numbers)
    return odd_numbers


def doubled_numbers(reduced_list):
    new_list = []
    for items in reduced_list:
        result = items ** 2
        new_list.append(result)
    return new_list


