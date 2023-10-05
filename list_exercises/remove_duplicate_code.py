duplicated_list = [15, 20, 25, 20, 10, 5 ]
removed_duplicated_list = []
for item in range(len(duplicated_list)):
    if duplicated_list[item]  not in removed_duplicated_list:
        removed_duplicated_list.append(duplicated_list[item])
print(removed_duplicated_list)