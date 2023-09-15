import random
count = 0
while count<3:
    play=int(input("Roll the dice"))
    dice=random.randint(1,6)
    if play == dice:
        print("You won!!")
    else:print("You loose")
    count +=1
