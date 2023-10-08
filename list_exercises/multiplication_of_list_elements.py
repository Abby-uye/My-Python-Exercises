def multuply_numbers(numbers):
    total = 0
    multiplication_of_elements = 1
    for item in range(len(numbers)):
        total += numbers[item]
        multiplication_of_elements = total * total
    return multiplication_of_elements