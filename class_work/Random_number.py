import random

number = int(input("Enter random number between 1 and ten:"))
guess = random.randint(1, 10)
while number != guess:

    number = int(input("Try again: "))

    if number == guess:
        print("Congratulations!!")
    # else:
    #     print("Congratulations")
