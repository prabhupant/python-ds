def is_palindrome(s) -> bool:
    return str(s)[::-1].lower() == str(s).lower()

print(is_palindrome(10001))
print(is_palindrome('adcbcda'))
print(is_palindrome('AdflLfDa'))
print(is_palindrome('HBaena'))
