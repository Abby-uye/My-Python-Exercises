import random


def random_number_generator():
    return random.randint(0, 11)


def random_number_multiplication():
    first_number = random_number_generator()
    second_number = random_number_generator()
    while True:
        print(f"Enter The correct answer {first_number} * {second_number} = ? ")
        answer = int(input())
        print(first_number, second_number)

        if answer == first_number * second_number:
            print("Correct answer, you did great ")
            first_number = random_number_generator()
            second_number = random_number_generator()
        else:
            print("Wrong answer try again")
            first_number = first_number
            second_number = second_number


numbers = random_number_multiplication()
print(numbers)
