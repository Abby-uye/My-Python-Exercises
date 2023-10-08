def duplicated_list(numbers):
    removed_duplicated_list = []
    for item in range(len(numbers)):
        if duplicated_list[item]  not in removed_duplicated_list:
            removed_duplicated_list.append(numbers[item])
    return removed_duplicated_list