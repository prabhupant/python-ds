"""
Luhn algorithm or Luhn formula is a simple checksum formula
used to validate a variety of identification numbers, such as
credit card numbers, IMEI numbers, National Provider Identifier numbers
in some of the Countries
"""

"""
It takes a number as an input
(Assuming cardnumber as a string)
and returns true or false
based upon whether number is valid or not
"""

def checkLuhn(cardNumber):
    cardLen = len(cardNumber)

    checkSum = 0

    isParity = False
    
    for digit in range(cardLen-1,-1,-1):
        if isParity:
            cal = int(cardNumber[digit])*2
        else:
            cal = int(cardNumber[digit])

        if cal>9:
            checkSum += cal -9
        else:
            checkSum += cal

        isParity = not isParity

    return checkSum%10==0
