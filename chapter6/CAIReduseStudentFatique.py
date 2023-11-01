import random


def generateRandomNumber():
    digit = random.randint(0, 11)
    return digit

def generateUserInputs():
    return int(input())

def generate_random_good_response():
    response = random.randint(1, 5)
    match response:
        case 1 : print("Very good!")
        case 2 :print("Excellent!")
        case 3 :print("Nice work!")
        case 4 :print("Keep up the good work!")
    return response


def generateRandomNotSoGoodResponse():
    response = random.randint(1, 5)
    match response:
        case 1 : print("No. Please try again.")
        case 2 :print("Wrong. Try once more.")
        case 3 :print("Don't give up!")
        case 4 : print("No. Keep trying.")
    return response
def randomMultiplication():
    firstNumber = generateRandomNumber()
    secondNumber = generateRandomNumber()
    while True:
        print(f"Enter the correct answer {firstNumber} * {secondNumber} =  ")
        answer = generateUserInputs()
        if answer == firstNumber * secondNumber:
            generate_random_good_response()
            firstNumber = generateRandomNumber()
            secondNumber = generateRandomNumber()
        else:
            generateRandomNotSoGoodResponse()
            firstNumber = firstNumber
            secondNumber = secondNumber

print(randomMultiplication())
