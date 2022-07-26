import time

startTime = time.time()
values = []

def bubbleSort(arr):

    swapped = False

    for n in range(len(arr)-1, 0, -1):
        for i in range(n):
            if arr[i] < arr[i + 1]:
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

            if not swapped:
                return

    print('\nsorted:\n')
    print(values)

fileObj = open('data2.txt', 'r')
values = fileObj.read().splitlines()
fileObj.close()
print('unsorted:\n')
print(values)

bubbleSort(values)

executeTime = (time.time() - startTime)
print('time elapsed: ' + str(executeTime))