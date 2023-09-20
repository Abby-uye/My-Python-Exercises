number = 0
print("number    square     cube")
for number in range(6):
    square = number * number
    cube = number * number * number
    number+=1

    print(f"{number:-3}  {square:-3}  {cube:-3}")