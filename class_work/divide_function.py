def square(number: int):
    remainder = number % 5
    the_square = number ** 0.50
    if number % 5 == 0:
        return the_square
    else:
        return remainder


print(square(36))
