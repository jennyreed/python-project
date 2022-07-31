import time 
import numpy as np
from matplotlib import pyplot as plt
startTime = time.time()
arr = []

def bubbleSort(arr):
    while (np.array_equal(arr, np.sort(arr)) == False):
   # while(sorted(arr) != arr):
        # Iterate from 0 to the length of the arr - 1
        for i in range(len(arr) - 1):
            # If the current item is greater than the next item, swap the items
            if(arr[i] > arr[i + 1]):
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    # Return the sorted array
    return arr

fileObj = open('data.txt', 'r')
arr = fileObj.read().splitlines()
fileObj.close()
data = np.array(arr).astype(np.float64)
print(bubbleSort(np.copy(data)))
#listCopy = list.copy(arr)
# bubbleSort(data)
# print('Unsorted arr\n')
# print(arr)
# bubbleSort(arr)
# print('\nSorted arr:\n')  
# print(arr)

executeTime = (time.time() - startTime)
print('Time taken to sort: ' + str(executeTime))

y_values = sorted

indexes = [0] * (len(arr))
for i in range(len(arr)):
    
    indexes[i] = i

x_values = indexes
#print(len(indexes))

# print sorted data in graph

sortedData = bubbleSort(np.copy(data))
plt.figure(1)
plt.scatter(indexes, sortedData)
plt.yticks(np.arange(min(sortedData), max(sortedData), 0.2))


#print unsorted data in graph

plt.figure(2)
plt.scatter(indexes, data)
plt.yticks(np.arange(min(data), max(data), 0.2))

#show graph

plt.show()
