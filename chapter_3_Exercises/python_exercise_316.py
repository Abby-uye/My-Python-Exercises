numbers = 0
large_number = 0
largest_number = 0
for numbers in range(1,11):
    userInput = int(input("enter an integer"))
    if numbers > large_number:
        large_number = numbers

    if largest_number < large_number:
        large_number = large_number

print("The largest nuber is" ,largest_number)
print("The second largest number is ",large_number)
