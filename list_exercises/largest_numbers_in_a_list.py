numbers = [15, 20, 25, 20, 10, 5]
largest = 0
for item in range(len(numbers)):
    if numbers[item] > largest:
        largest = numbers[item]
print("The largest number is ", largest)