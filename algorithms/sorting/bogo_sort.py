import random 
 
def bogoSort(a): 
	n = len(a) 
	while (is_sorted(a)== False): 
		shuffle(a) 
 
def is_sorted(a): 
	n = len(a) 
	for i in range(0, n-1): 
		if (a[i] > a[i+1] ): 
			return False
	return True
 
def shuffle(a): 
	n = len(a) 
	for i in range (0,n): 
		r = random.randint(0,n-1) 
		a[i], a[r] = a[r], a[i] 
 
test_array = [99, 11, 78, 10, 0, 54, 67] 
bogoSort(test_array)

print(
    "Sorting 99, 11, 78, 10, 0, 54, 67...\n" +
    "Please Wait...\n"
    )
    
for i in range(len(test_array)): 
	print (test_array[i])