import time
startTime = time.time()

sortedArray = []

def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min = i
        for j in range(i + 1, n):
            if(lst[j] < lst[min]):
                min = j
        lst[i], lst[min] = lst[min], lst[i]
        

fileObj = open('data2.txt', 'r')
array = fileObj.read().splitlines()
fileObj.close()
print('Unsorted Array:\n')
print(array)
selection_sort(array)
print('Sorted arr:\n')
print(array)


executeTime = (time.time() - startTime)
print('Time taken to sort: ' + str(executeTime))