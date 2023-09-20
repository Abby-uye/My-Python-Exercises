number = 1

print("number square  cube")
while number <= 10:
    square = number * number
    cube = number * number * number
    print(f"{number}   {square:>5}   {cube:>5}")
    number+=1