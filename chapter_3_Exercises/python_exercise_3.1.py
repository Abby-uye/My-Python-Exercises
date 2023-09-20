passes = 0
failures = 0
counter = 0
for student in range(10):
    result =int(input("Enter result (1=pass,2=fail): "))
    while result != 1 and result !=2:
        result = int(input("Enter result (1=pass,2=fail): "))

        result = result


    if result == 1:
        passes+=1


    elif result == 2:
        failures+=1

    counter +=1

print("passed",passes)
print("Failed",failures)

if passes > 8:
    print("bonus to facilitator")
