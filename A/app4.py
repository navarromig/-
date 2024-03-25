import numpy as np

Points = [(np.random.uniform(0,200),np.random.uniform(0,200)) for i in range(100)]
List_points = np.array(Points)
print("List of points:")
print(List_points)

import matplotlib.pyplot as plt

def plot2D(List_points,L):
  plt.figure(figsize=(10,10))
  x = List_points[:,0]        #x coordinate for P
  y = List_points[:,1]        #y coordinate for P
  plt.plot(x,y,'.k')  #plot all the points
  x = L[:,0]
  y = L[:,1]
  plt.plot(x,y,'b-')      #plot points of convex hull using coordinates x and y
  xlast = [L[len(x)-1,0],L[0,0]]
  ylast = [L[len(x)-1,1],L[0,1]]
  plt.plot(xlast, ylast, 'b-')    #plot last vertex
  plt.title("Convex hull")
  plt.show()

from quick_hull import quickhull
from scipy.spatial import convex_hull_plot_2d


List_points = np.array(Points)
L = quickhull(Points)
print("Points of convex hull:")
print(List_points[L.vertices])
fig, ax = plt.subplots(figsize=(10,10))
_ = convex_hull_plot_2d(L,ax)
plt.show()