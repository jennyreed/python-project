import time
startTime = time.time()
arr = []

def bubbleSort(arr):

    # swapped = False

    # for n in range(len(arr)-1, 0, -1):
    #     for i in range(n):
    #         if arr[i] < arr[i + 1]:
    #             swapped = True
    #             arr[i], arr[i + 1] = arr[i + 1], arr[i]

    #         if not swapped:
    #             return arr
    # return arr

    while(sorted(arr) != arr):
        # Iterate from 0 to the length of the arr - 1
        for i in range(len(arr) - 1):
            # If the current item is greater than the next item, swap the items
            if(arr[i] > arr[i + 1]):
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
    # Return the sorted array
    return arr

fileObj = open('data2.txt', 'r')
arr = fileObj.read().splitlines()
fileObj.close()
listCopy = list.copy(arr)
bubbleSort(listCopy)
print('Unsorted arr\n')
print(arr)
bubbleSort(arr)
print('\nSorted arr:\n')  
print(arr)

executeTime = (time.time() - startTime)
print('Time taken to sort: ' + str(executeTime))

