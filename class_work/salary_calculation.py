def your_salary(name,number_of_periods):
    hours_worked = 100
    salary = 0
    rate_per_period =20
    over_time = 25
    calculator = 0
    if number_of_periods > hours_worked:
        calculator = number_of_periods - hours_worked
        salary = hours_worked*rate_per_period+(calculator*over_time)
    elif number_of_periods < hours_worked:
        salary = number_of_periods * rate_per_period
    return salary


the_test = your_salary("Abby",50)
print(the_test)