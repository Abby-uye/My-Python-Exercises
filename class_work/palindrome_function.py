def palindrome(userinput):
    former_number = userinput
    r = 0
    while userinput != 0:
        number = userinput % 10
        r = r * 10 + number
        userinput //= 10
    if former_number == r:
        return True
    else:
        return False

