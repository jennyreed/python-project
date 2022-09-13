import time
startTime = time.time()
a= []

def insertsort(a):
  
    # traversing the array from 1 to length of the array(a)
    for i in range(1, len(a)):
  
        temp = a[i]
  
        j = i-1
        while j >=0 and temp < a[j] :
                a[j+1] = a[j]
                j -= 1
        a[j+1] = temp
    return a
     
fileObj = open('data2.txt', 'r')
a = fileObj.read().splitlines()
fileObj.close()
print('Unsorted arr\n')
print(a)
insertsort(a)
print('\nSorted arr:\n')  
print(a)

executeTime = (time.time() - startTime)
print('Time taken to sort: ' + str(executeTime))
