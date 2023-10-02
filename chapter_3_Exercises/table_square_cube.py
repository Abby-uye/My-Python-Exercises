print("number   square     cube")
for number in range (1,6):
    square = number * number
    cube = number * number *number
    square+=1
    cube +=1
    print(f"{number:>6}    {square:>5}  {cube:>5}")