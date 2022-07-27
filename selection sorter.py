import time
startTime = time.time()
array = []
sortedArray = []

def selectionSort(arr):
    
    for i in range(len(arr)):
        smallestVal = min(arr)
        sortedArray.append(smallestVal)
        array.remove(min(array))
        
    print('\nSorted Array:\n')
    print(sortedArray)



fileObj = open('data2.txt', 'r')
array = fileObj.read().splitlines()
fileObj.close()
print('Unsorted Array:\n')
print(array)

selectionSort(array)

executeTime = (time.time() - startTime)
print('Time taken to sort: ' + str(executeTime))