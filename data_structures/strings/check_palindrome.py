# function to check string is  
# palindrome or not  
def isPalindrome(str): 
  
    # Run loop from 0 to len/2  
    for i in xrange(0, len(str)/2):  
        if str[i] != str[len(str)-i-1]: 
            return False
    return True
