user_input = input("Enter a letter to know if it is a vowel or not: ")
match user_input:
    case "A":
        print("vowel")
    case "a":
        print("vowel")
    case "E":
        print("vowel")
    case "e":
        print("Vowel")
    case "I":
        print("Vowel")
    case "i":
        print("Vowel")
    case "U":
        print("vowel")
    case"u":
        print("Vowel")

    case _:
        print("consonant")
