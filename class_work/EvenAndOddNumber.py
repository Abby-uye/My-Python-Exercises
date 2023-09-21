count_even = 0
counter_odd = 0
for number in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(number, end= "")

    if number % 2 == 0:
        count_even += 1
    elif number % 2 == 1:
        counter_odd += 1
print(f"\n The number of even numbers is ", count_even)
print("The number of odd numbers is ", counter_odd)
