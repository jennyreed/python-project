import time
startTime = time.time()
array = []

def bubbleSort(arr):

    swapped = False

    for n in range(len(arr)-1, 0, -1):
        for i in range(n):
            if arr[i] < arr[i + 1]:
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

            if not swapped:
                return

    print('\nSorted Array:\n')
    print(array)
    return arr

fileObj = open('data2.txt', 'r')
array = fileObj.read().splitlines()
fileObj.close()
print('Unsorted Array\n')
print(array)

bubbleSort(array)

executeTime = (time.time() - startTime)
print('Time taken to sort: ' + str(executeTime))