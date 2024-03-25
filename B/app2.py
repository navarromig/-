def plotPointsRect(Par, R):
  plt.figure(figsize=(10,10))
  x = Par[:,0]        #x coordinate for P
  y = Par[:,1]        #y coordinate for P
  plt.plot(x,y,'.b')  #plot all the points
  xr = [R[0][0],R[0][0],R[1][0],R[1][0],R[0][0]]  #plot rectangle
  yr = [R[0][1],R[1][1], R[1][1], R[0][1], R[0][1]]
  plt.plot(xr,yr,'-k')
  plt.title('Points and rectangle')
  plt.show()

import numpy as np
import matplotlib.pyplot as plt

Points = [(np.random.uniform(0,200),np.random.uniform(0,200)) for i in range(70)]
List_points = np.array(Points)
print("List of points:")
print(List_points)

from search_kd import createKd, searchKd

root = createKd(Points)
infreg = ((-float("inf"),float("inf")),(-float("inf"),float("inf")))  #((xleft,xright),(ydown,yup))
R = ((40.0,70.0),(120.0,180.0))   #((xmin,ymin),(xmax, ymax)) for rectangle
leaves = []
searchKd(root, infreg, R, leaves)
print('Number of points into the rectangle: ', len(leaves))
print('Points into the rectangle: ', *leaves, sep = "\n") #points into the rectangle
plotPointsRect(List_points, R)
