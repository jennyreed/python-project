from random import randint, random

from numpy import average
from bubblesorter import bubbleSort, arr
from time import time

averagecase = arr
#averagecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(averagecase)
worstcase= sorted(averagecase, reverse=True)


def test_BubbleWorst():
    start= time()
    assert bubbleSort(list.copy(worstcase)) == bestcase
    print(time()-start)
 
def test_BubbleBest():
    start= time()
    assert bubbleSort(list.copy(bestcase)) == bestcase
    print(time()-start)
 
def test_BubbleAvg():
    start= time()
    assert bubbleSort(list.copy(averagecase)) == bestcase
    print(time()-start)