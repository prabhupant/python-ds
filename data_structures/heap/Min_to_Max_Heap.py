# A Python3 program to convert min Heap 
# to max Heap 
def MaxHeapify(arr, i, n): 
	l = 2 * i + 1
	r = 2 * i + 2
	largest = i 
	if l < n and arr[l] > arr[i]: 
		largest = l 
	if r < n and arr[r] > arr[largest]: 
		largest = r 
	if largest != i: 
		arr[i], arr[largest] = arr[largest], arr[i] 
		MaxHeapify(arr, largest, n) 
def convertMaxHeap(arr, n): 
	for i in range(int((n - 2) / 2), -1, -1): 
		MaxHeapify(arr, i, n) 
def printArray(arr, size): 
	for i in range(size): 
		print(arr[i], end = " ") 
	print() 

if __name__ == '__main__': 
	arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9] 
	n = len(arr) 

	print("Min Heap array : ") 
	printArray(arr, n) 

	convertMaxHeap(arr, n) 

	print("Max Heap array : ") 
	printArray(arr, n) 

