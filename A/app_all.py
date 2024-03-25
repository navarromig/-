import numpy as np

Points = [(np.random.uniform(0,200),np.random.uniform(0,200)) for i in range(100)]
List_points = np.array(Points)
print("List of points:")
print(List_points)

import matplotlib.pyplot as plt

def plot2D(List_points,L):
  plt.figure(figsize=(10,10))
  x = List_points[:,0]        #coordinate-x 
  y = List_points[:,1]        #coordinate-y 
  plt.plot(x,y,'.b', markersize=10)  #plotting all the points for Points
  x = L[:,0]
  y = L[:,1]
  plt.plot(x,y,'k-', markersize=10)      #plotting points of Convex Hull
  last_x = [L[len(x)-1,0],L[0,0]]
  last_y = [L[len(x)-1,1],L[0,1]]
  plt.plot(last_x, last_y, 'k-', markersize=10)    #plotting last vertex
  plt.title("Convex Hull Diagram")
  plt.show()

List_points = np.array(Points) 

from incr import incremental

L1 = incremental(Points)
print("Points of convex hull with Incremental:")
print(L1)
plot2D(List_points,L1)


from g_wrp import giftwrapping

L2 = giftwrapping(Points)
print("Points of convex hull with Gift Wrapping:")
print(L2)
plot2D(List_points,L2)


from div_con import divideConquer

L3 = divideConquer(Points)
print("Points of convex hull Divide and conquier:")
print(np.array(L3))
plot2D(List_points,np.array(L3))

from quick_hull import quickhull
from scipy.spatial import convex_hull_plot_2d

L4 = quickhull(Points)
print("Points of convex hull with QuickHull:")
print(List_points[L4.vertices])
fig, ax = plt.subplots(figsize=(10,10))
_ = convex_hull_plot_2d(L4,ax)
plt.show()
