
count = 1
total = 0
score = int(input("Enter your score To stop press -1: "))
while score != -1:
    count += 1
    total = total + score
    score = int(input("Enter your score To stop press -1: "))
average = total / count
print("Average is ", average)
print("Total is", total)
