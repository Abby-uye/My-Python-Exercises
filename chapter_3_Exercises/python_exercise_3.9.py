numbers = int(input("Enter a number: "))
count = 5
while count >0:
    count -= 1
    digit = numbers // 10** count % 10
    print(digit, end= " ")

