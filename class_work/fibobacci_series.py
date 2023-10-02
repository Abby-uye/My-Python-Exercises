
def fibonacci(fib_number):
    number = 0
    counter = 0
    total = counter + number

    while counter < fib_number:
        print(total, end=" ")
        counter = number
        number = total
        total = counter + number

    return total



