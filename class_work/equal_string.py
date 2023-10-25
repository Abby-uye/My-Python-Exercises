def string_equal(letters,characters):
    is_equal = False
    for item in letters:
        for items in characters:
            if len(item) == len(items):
                if item == items:
                    is_equal =True
        return is_equal

print(string_equal("Hello","Hello"))