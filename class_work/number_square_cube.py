number = 0
print("number    square    cube")
for number in range(1, 11):
    square_of_number = number * number
    cube_of_number = number * number * number

    print(f" {number:}  {square_of_number:>8}  {cube_of_number:>8}")
