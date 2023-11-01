def list_to_dictionary(letters):
    dictionary = {}
    key = ""
    for items in letters:
        key = items[0]
        if key in dictionary.keys():
            the_key = key
            the_key = the_key.upper()
            dictionary[the_key] = items
        else:
            dictionary[key] = items
    return dictionary


def difference(numbers):
    smallest_number = numbers[0]
    largest_number = numbers[0]
    for items in numbers:
        if items < smallest_number:
            smallest_number = items
        if items > largest_number:
            largest_number = items
    the_difference = largest_number - smallest_number
    return the_difference


the_list = [10, 75, 20, 30, 15, 5, 40, 25, 40, 35]
result = difference(the_list)
print(result)
