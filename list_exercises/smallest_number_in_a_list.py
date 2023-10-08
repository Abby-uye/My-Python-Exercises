
def smallest_numbers (numbers):
    smallest_number = numbers[0]
    for item in range(len(numbers)):
        if numbers[item] < smallest_number:
            smallest_number = numbers[item]
    return smallest_number

numbers = [15, 20, 25, 20, 10, 5]
smallest_number = numbers[0]
for item in range(len(numbers)):
    if numbers[item] < smallest_number:
        smallest_number = numbers[item]
print("The smallest number is ", smallest_number)

