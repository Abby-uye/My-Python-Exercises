def lcm(number)
    divisor = 0
    list_of_divisors = []
    while number >1:
        if number % divisor == 0:
            list_of_divisors.append(divisor)
            number = number / divisor
        else:divisor+=1
    return list_of_divisors