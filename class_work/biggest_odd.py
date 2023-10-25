def big_numbers(numbers):
    max = 0
    for number in numbers:
        the_number = int(number)
        if the_number % 2 != 0:
            if the_number > max:
                max = the_number
    return max

print(big_numbers("23569"))