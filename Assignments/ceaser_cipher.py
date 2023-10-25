def encrypt(letters):
    enctrypted = ""
    for characters in letters:
        the_character = [ord(characters)+3]
        enctrypted .join[chr(the_character)]
    return enctrypted


print(encrypt("Hello"))
