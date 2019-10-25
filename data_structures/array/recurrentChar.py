#Find out and print First Recurrent character from given string 


def recc_char(strng):
    prev = set()
    for char in strng:
        if char in prev:
            print (char)
            return char
        prev.add(char)

    return None

recc_char("acbbac")



