number = 0
counter = 1
total = number + counter
for number in range (50):
    print(total)
    total = number + counter
    number = counter
    counter = number
    number+=1

    if number == 50:
        break