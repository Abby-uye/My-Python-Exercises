first_number =int(input("Enter a number"))
second_number = int(input("Enter a number"))
third_number = int(input("Enter a number"))
sum = first_number + second_number +third_number
average = first_number + second_number +third_number /100
product = first_number * second_number * third_number
print( sum)
print (average)
print(product)
if first_number > second_number and first_number > third_number:
	print("first_number is the largest number")
if first_number < second_number and first_number < third_number:
	print("first number is the smallest number")
if second_number > first_number and second_number >third_number:
	print("secon number is the largest number")
if second_number < first_number and second_number < third_number:
	print("second number is the smallest number")
if third_number > first_number and third_number > second_number:
	print(" third number is the largest number")
if third_number < first_number and third_number < second_number:
	print("third_number is the smallest number")