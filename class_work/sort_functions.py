def sort_function(list1: list,):
    the_sorted =[]
    for item in list1:

        if list1[item] < the_sorted[item]:
            the_sorted = list1[item]
    return the_sorted
the_list = [3,6,7,3,8]
print(sort_function(the_list))


