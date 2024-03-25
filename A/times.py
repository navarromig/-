import time
import copy
import numpy as np

from incr import incremental
from g_wrp import giftwrapping
from div_con import divideConquer
from quick_hull import quickhull

########################### 100 points ##########################


Points1 = [(np.random.uniform(0,200),np.random.uniform(0,200)) for i in range(100)]

P1_1 = copy.deepcopy(Points1)
P1_2 = copy.deepcopy(Points1)
P1_3 = copy.deepcopy(Points1)
P1_4 = copy.deepcopy(Points1)

tstart = time.time()
L1_1 = incremental(P1_1)
tend = time.time()
t1_1 = tend-tstart

tstart = time.time()
L1_2 = giftwrapping(P1_2)
tend = time.time()
t1_2 = tend-tstart

tstart = time.time()
L1_3 = divideConquer(P1_3)
tend = time.time()
t1_3 = tend-tstart

tstart = time.time()
L1_4 = quickhull(P1_4)
tend = time.time()
t1_4 = tend-tstart


########################### 1000 points ##########################


Points2 = [(np.random.uniform(0,200),np.random.uniform(0,200)) for i in range(1000)]

P2_1 = copy.deepcopy(Points2)
P2_2 = copy.deepcopy(Points2)
P2_3 = copy.deepcopy(Points2)
P2_4 = copy.deepcopy(Points2)

tstart = time.time()
L2_1 = incremental(P2_1)
tend = time.time()
t2_1 = tend-tstart

tstart = time.time()
L2_2 = giftwrapping(P2_2)
tend = time.time()
t2_2 = tend-tstart

tstart = time.time()
L2_3 = divideConquer(P2_3)
tend = time.time()
t2_3 = tend-tstart

tstart = time.time()
L2_4 = quickhull(P2_4)
tend = time.time()
t2_4 = tend-tstart

########################### 10000 points ##########################


Points3 = [(np.random.uniform(0,200),np.random.uniform(0,200)) for i in range(10000)]

P3_1 = copy.deepcopy(Points3)
P3_2 = copy.deepcopy(Points3)
P3_3 = copy.deepcopy(Points3)
P3_4 = copy.deepcopy(Points3)

tstart = time.time()
L3_1 = incremental(P3_1)
tend = time.time()
t3_1 = tend-tstart

tstart = time.time()
L3_2 = giftwrapping(P3_2)
tend = time.time()
t3_2 = tend-tstart

tstart = time.time()
L3_3 = divideConquer(P3_3)
tend = time.time()
t3_3 = tend-tstart

tstart = time.time()
L3_4 = quickhull(P3_4)
tend = time.time()
t3_4 = tend-tstart


########################### 100000 points ##########################


Points4 = [(np.random.uniform(0,200),np.random.uniform(0,200)) for i in range(100000)]


P4_1 = copy.deepcopy(Points4)
P4_2 = copy.deepcopy(Points4)
P4_3 = copy.deepcopy(Points4)
P4_4 = copy.deepcopy(Points4)


tstart = time.time()
L4_1 = incremental(P4_1)
tend = time.time()
t4_1 = tend-tstart

tstart = time.time()
L4_2 = giftwrapping(P4_2)
tend = time.time()
t4_2 = tend-tstart

tstart = time.time()
L4_3 = divideConquer(P4_3)
tend = time.time()
t4_3 = tend-tstart

tstart = time.time()
L4_4 = quickhull(P4_4)
tend = time.time()
t4_4 = tend-tstart



print("{:<20} {:<25} {:<25} {:<25} {:<25}".format('Points','100 points','1000 points','10000 points', '100000 points'))
print("{:<20} {:<25} {:<25} {:<25} {:<25}".format('Incremental', t1_1, t2_1, t3_1, t4_1))
print("{:<20} {:<25} {:<25} {:<25} {:<25}".format('Gift Wrapping',t1_2, t2_2, t3_2, t4_2))
print("{:<20} {:<25} {:<25} {:<25} {:<25}".format('Divide and Conquer',t1_3, t2_3, t3_3, t4_3))
print("{:<20} {:<25} {:<25} {:<25} {:<25}".format('QuickHull',t1_4, t2_4, t3_4, t4_4))