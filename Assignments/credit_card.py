def check_credit_card_type(credit_card_number):
    card_type = ""
    match credit_card_number[0]:
        case 4:
            card_type = "Visa Card"
        case 5:
            card_type = "Master Card"
        case 37:
            card_type = "American Express Card"
        case 6:
            card_type = "Discovery Card"
    return card_type


def even_position(credit_card_number):
    position = 0
    for index, value in enumerate(credit_card_number):
        if index % 2 == 0:
            value = credit_card_number[index] * 2
            if value > 9:
                the_modulo = int(value % 2)
                result = int(value / 2)
                position += int(the_modulo + result)
            else:
                position += int(value)
        return position
