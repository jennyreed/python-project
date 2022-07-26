# Python program for implementation of Bubble Sort
import time
startTime = time.time()
values = []

def bubbleSort(arr):
	n = len(arr)
	swapped = False
	for i in range(n-1):
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
	
		if not swapped:
		
			return

fileObj = open('data.txt', 'r')
arr = fileObj.read().splitlines()
fileObj.close()
print('unsorted:\n')
print(arr)

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
	print("% d" % arr[i], end=" ")
    
