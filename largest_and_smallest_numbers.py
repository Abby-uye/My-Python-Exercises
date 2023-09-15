userInput = int(input("Enter a number: "))
largest_number = userInput
smallest_number = userInput
while userInput != -1:
    userInput = int(input("To stop press -1: "))
    if userInput > largest_number:
        largest_number = userInput
    elif userInput < smallest_number and userInput != -1:
        smallest_number = userInput
print("The largest number is ",largest_number)
print("The smallest number is ",smallest_number)


