userInput = int(input("Enter a number: "))
zero = 0
positive = 0
negative = 0
while userInput != -1:
    userInput = int(input("To stop enter -1  "))
    if userInput == 0:
        zero += 1
    elif userInput > 0:
        positive = positive + 1
    elif userInput < 0 and userInput != -1:
         negative = negative + 1

print("The number of negative number is ",negative)
print("The number of positive number is ", positive)
print("The number of zero number is",zero)
