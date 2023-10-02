def even_odd(list_user_input):
    count_even = 0
    counter_odd = 0
    for number in list_user_input:
        print(number, end= "")

        if number % 2 == 0:
            count_even += 1
            return print(f"\n The number of even numbers is ", count_even)

        elif number % 2 == 1:
            counter_odd += 1
        return print("The number of odd numbers is ", counter_odd)
