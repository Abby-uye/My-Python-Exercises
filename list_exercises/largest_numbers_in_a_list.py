<<<<<<< HEAD
def largest_numbers(numbers):
    largest = numbers[0]
    for item in range(len(numbers)):
        if numbers[item] > largest:
            largest = numbers[item]
    return largest
=======
numbers = [15, 20, 25, 20, 10, 5]
largest = 0
for item in range(len(numbers)):
    if numbers[item] > largest:
        largest = numbers[item]
print("The largest number is ", largest)

# good, pls give me another algorithm below
# leave the one above and write another solution below this comment
>>>>>>> 95af2e26ec1c42af03c07f6ed99f35e92a2106e7
