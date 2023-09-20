
largest_number = 0
smallest_number = 0
sum = 0
average = sum / 4


for number in range(4):
    number1 = int(input("Enter a number and will calculate it for you: "))

    if number1 > largest_number:
        largest_number = number1

    if number1 < smallest_number:
        smallest_number = number1

    sum = sum + number1
    average += 1

print("The largest number is: ",largest_number)
print("The smallest number is: ", smallest_number)
print("The sum of the numbers is :",sum)
print("The average of the number is:",average)