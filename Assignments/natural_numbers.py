number = int(input("Enter ten natural numbers: "))
natural_numbers_count =1
total = 0
number = 1
while natural_numbers_count <=10:
    if number > 0:
        number = int(input("Enter another number"))
        total  += number
    elif number < 0:
        print("Enter a positive number")
    natural_numbers_count+=1
print(total)