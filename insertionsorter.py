import time
startTime = time.time()

def InsertionSort(a):
  
    # traversing the array from 1 to length of the array(a)
    for i in range(1, len(a)):
  
        temp = a[i]
  
        # Shift elements of array[0 to i-1], that are
        # greater than temp, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and temp < a[j] :
                a[j+1] = a[j]
                j -= 1
        a[j+1] = temp

        
fileObj = open('data2.txt', 'r')
a = fileObj.read().splitlines()
fileObj.close()
InsertionSort(a)
print("Array after sorting:")
print(a)

executeTime = (time.time() - startTime)
print('Time taken to sort: ' + str(executeTime))
