numbers = [15, 20, 25, 20, 10, 5 ]
total = 0
multiplication_of_elements = 1
for item in range(len(numbers)):
    total += numbers[item]
    multiplication_of_elements = total * total
print(multiplication_of_elements)