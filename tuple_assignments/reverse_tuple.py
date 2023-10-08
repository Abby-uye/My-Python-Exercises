def reverse_tuple(numbers):
    new_list = []
    new_tuple = ()
    for item in range (1,len(numbers) +1):
        new_list.append(numbers[-item])
    for item in new_list:
        new_tuple +=(item,)

    return new_tuple


print(reverse_tuple((1,3,6,7)))