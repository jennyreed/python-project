from random import randint, random
from numpy import average
from selectionsorter import selection_sort, array
from time import time

averagecase = array
#averagecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(averagecase)
worstcase= sorted(averagecase, reverse=True)


def test_SelectWorst():
    start= time()
    assert selection_sort(list.copy(worstcase)) == bestcase
    print(time()-start)
 
def test_SelectBest():
    start= time()
    assert selection_sort(list.copy(bestcase)) == bestcase
    print(time()-start)
 
def test_SelectAvg():
    start= time()
    assert selection_sort(list.copy(averagecase)) == bestcase
    print(time()-start)
