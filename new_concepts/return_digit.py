def digit_count(numbers):
    count = 0
    for item in numbers:
        characters = item
        for index in characters:
            if index == '0' or index == '1' or index == '2' or index == '3' or index == '4' or index =='5' or index == '6' or index == '7' :
                count += 1
    return count


the_characters = ["Abc21f", "13cpz", 'a1l']
print(digit_count(the_characters))
