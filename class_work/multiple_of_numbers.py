def fizbuzz(digits):
    fizz = 0
    buzz = 0
    fizzbuzz = 0
    for number in range(digits):
        if number % 3 == 0 and number % 5 == 0:
         print("FizzBuzz")
         fizzbuzz+=1
         return fizzbuzz
        elif number % 3 == 0:
            print("Fizz")
            fizz+=1
            return fizz
        elif number % 5 == 0:
            print("Buzz")
            buzz+=1
            return buzz
        else:
            print(number)
            number+=1
            return number

