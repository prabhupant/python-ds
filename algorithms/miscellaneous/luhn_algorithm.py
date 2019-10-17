def check_luhn(card_number):
    """
    Luhn algorithm or Luhn formula is a simple checksum formula
    used to validate a variety of identification numbers, such as
    credit card numbers, IMEI numbers, National Provider Identifier numbers
    in some of the countries.

    It takes a number as an input
    (Assuming cardnumber as a string)
    and returns true or false
    based upon whether number is valid or not

    :param card_number:
    :return: bool: valid or not

    Examples:

    >>> check_luhn("950123440000")
    False
    >>> check_luhn("490154203237518")
    True
    """
    card_len = len(card_number)

    check_sum = 0

    is_parity = False

    for digit in range(card_len - 1, -1, -1):
        if is_parity:
            cal = int(card_number[digit]) * 2
        else:
            cal = int(card_number[digit])

        if cal > 9:
            check_sum += cal - 9
        else:
            check_sum += cal

        is_parity = not is_parity

    return check_sum % 10 == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
