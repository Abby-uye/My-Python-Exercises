def numbers(number):
    largest = 0
    for item in number:
        if item > largest:
            largest = item
    return largest


def reverse_list(number):
    number.reverse()
    return numbers


def check_elements(number, item):
    if item in number:
        return True
    else:
        return False


def elements_in_odd_position(number):
    odd_position = len(number/2)
    for item in range(1, len(number), 2):
        odd_position= number[item]
        return odd_position

def running_total(number):
    total = 0
    for item in range (len(number)):
        total = total + number[item]
        return total