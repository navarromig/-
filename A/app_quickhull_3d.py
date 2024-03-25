import numpy as np

Points = [(np.random.uniform(0,200),np.random.uniform(0,200),np.random.uniform(0,200)) for i in range(80)]
List_points = np.array(Points)
print("List of List_points:")
print(List_points)

import matplotlib.pyplot as plt
from matplotlib import axis

def plot3D(List_points,L):
  fig = plt.figure(figsize=(8,8))
  ax = fig.add_subplot(projection='3d')
  x = List_points[:,0]
  y = List_points[:,1]
  z = List_points[:,2]
  ax.scatter(x,y,z,c='k')
  for s in L.simplices:
      simplices = np.append(s, s[0])
      x = List_points[s, 0]
      y = List_points[s, 1]
      z = List_points[s, 2]
      ax.plot(x,y,z,'b-')

  plt.show()

from quick_hull_3d import quickhull3d

L = quickhull3d(Points)
print("List_points of convex hull:")
print(List_points[L.vertices])
plot3D(List_points,L)