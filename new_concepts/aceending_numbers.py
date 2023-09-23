list_of_numbers = [4,9,8,6,4,3,2,]
for index1 in range (0,len(list_of_numbers)):
    for index2 in range(index1+1,len(list_of_numbers)):
        if list_of_numbers[index1] > list_of_numbers[index2]:
            list_of_numbers [index1], list_of_numbers[index2]= list_of_numbers[index2],list_of_numbers[index1]
print(list_of_numbers)