def largest_numbers(numbers):
    largest = numbers[0]
    for item in range(len(numbers)):
        if numbers[item] > largest:
            largest = numbers[item]
    return largest