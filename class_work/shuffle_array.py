def character_array(characters):
    x = characters[0::3]
    y = characters[1::3]
    z = characters[2::3]
    result = x+y+z
    return result
print(character_array(['A','M','C','W','I','T']))