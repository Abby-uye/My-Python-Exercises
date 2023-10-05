numbers = [15, 20, 25, 20, 10, 5]
smallest_number = 10000
for item in range(len(numbers)):
    if numbers[item] < smallest_number:
        smallest_number = numbers[item]
print("The largest number is ", smallest_number)