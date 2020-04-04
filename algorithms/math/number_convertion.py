bases = {
    "binary": 2,
    "octal": 8,
    "decimal": 10,
    "hex": 16,
    "hexadecimal": 16
}

default = 10


def verify_base(x):
    """
    Verify if already is an integer
    If is not verify if is in the bases
    If is not return the default base
    """
    try:
        return int(x)
    except:
        if x in bases:
            return bases[x]
        else:
            return default


def decimal_value(x):
    """
    ord(x) is a function that return the number in asc2 table
    we use ord to get the number of an caracter
    """
    # TODO verify if in the base exist the character like:
    # 'z' doesnt exisist in decimal values
    if(x >= '0' and x <= '9'):
        return int(x)
    elif(x >= 'a' and x <= 'z'):
        return int(ord(x) - ord('a') + 10)
    elif(x >= 'A' and x <= 'Z'):
        return int(ord(x) - ord('A') + 10)
    else:
        # Error
        raise Exception('Number not valid for: ', x)


def to_special_caracter(x):
    if(x >= 0 and x <= 9):
        return str(x)
    elif(x > 9):
        return chr(ord('a') + x - 10)
    else:
        raise Exception('Not valid negative number in converter: ', x)


def convert(n, from_base, to_base):
    """
    This algorithm convert numbers between any base to any base like:

    convert("10",2,10)
    ~> "2"

    This function recive 3 parameters
    n -> the number
    from_base -> base of n |
    to_base -> base of the result |
    you can pass the bases as number like base 2 or as string like "binary"

    Why the n and the return is an string?
    Because bases greater the 10 use leathers to represents the numbers
    """
    n = str(n)
    from_base = verify_base(from_base)
    to_base = verify_base(to_base)

    # Corner case 0
    if(n == "0"):
        return n

    if(n[0] == '-'):
        n = n[1:]
        negative = True
    else:
        negative = False

    # We convert to decimal because is the easy way to convert to all
    multi = 1
    decimal_number = 0
    if(from_base == 10):
        decimal_number = int(n)
    else:
        for i in range(len(n) - 1, -1, -1):
            decimal_number += (multi * decimal_value(n[i]))
            multi *= from_base

    if(to_base == 10):
        decimal_number = str(decimal_number)
        if(negative):
            decimal_number = '-' + decimal_number

        return decimal_number

    result = ""

    while(decimal_number > 0):
        value = decimal_number % to_base
        result = to_special_caracter(value) + result
        decimal_number = int((decimal_number - value)/to_base)

    if(negative):
            result = '-' + result

    return result


def test_convert():
    print(convert("1111000111", 2, 8) == "1707")
    print(convert("1111000111", 2, 10) == "967")
    print(convert("1111000111", 2, 16) == "3c7")
    print(convert("1234567", 8, 2) == "1010011100101110111")
    print(convert("1234567", 8, 10) == "342391")
    print(convert("1234567", 8, 16) == "53977")
    print(convert("987123", 10, 2) == "11110000111111110011")
    print(convert("987123", 10, 8) == "3607763")
    print(convert("987123", 10, 16) == "f0ff3")
    print(convert("abcdef", 16, 2) == "101010111100110111101111")
    print(convert("abcdef", 16, 8) == "52746757")
    print(convert("abcdef", 16, 10) == "11259375")

    print(convert("179", 10, 16) == "b3")
    print(convert("b3", 16, 10) == "179")

    # Negative Tests
    print("Negative Tests")
    print(convert("-179", 10, 16) == "-b3")
    print(convert("-b3", 16, 10) == "-179")
    print(convert("-1111000111", 2, 10) == "-967")

test_convert()
