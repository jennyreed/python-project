import time
startTime = time.time()

def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
fileObj = open('data2.txt', 'r')
array = fileObj.read().splitlines()
fileObj.close()
size = len(array)
print('Unsorted Array:\n')
print(array)
selectionSort(array, size)
print('Sorted arr:\n')
print(array)



executeTime = (time.time() - startTime)
print('Time taken to sort: ' + str(executeTime))