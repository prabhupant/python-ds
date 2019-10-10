"""
Question : Swap commas and dots in a String
Examples:

Input : 14, 625, 498.002
Output : 14.625.498, 002

"""
# This propler can be solved via two popular ways
# Using replace()
def Replace(str1): 
	str1 = str1.replace(', ', 'third') 
	str1 = str1.replace('.', ', ') 
	str1 = str1.replace('third', '.') 
	return str1 
	
string = "14, 625, 498.002"
print(Replace(string)) 
# Using maketrans and translate()
def Replace(str1): 
	maketrans = str1.maketrans 
	final = str1.translate(maketrans(', .', '., ')) 
	return final 

