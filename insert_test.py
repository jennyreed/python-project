from random import randint, random
from numpy import average
from insertionsorter import insertsort, a
from time import time

averagecase = a
#averagecase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(averagecase)
worstcase= sorted(averagecase, reverse=True)


def test_SelectWorst():
    start= time()
    assert insertsort(list.copy(worstcase)) == bestcase
    print(time()-start)
 
def test_SelectBest():
    start= time()
    assert insertsort(list.copy(bestcase)) == bestcase
    print(time()-start)
 
def test_SelectAvg():
    start= time()
    assert insertsort(list.copy(averagecase)) == bestcase
    print(time()-start)