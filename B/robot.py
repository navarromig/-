def plotPointsRect(Par, R):
  plt.figure(figsize=(10,10))
  x = Par[:,0]        #x coordinate for P
  y = Par[:,1]        #y coordinate for P
  plt.plot(x,y,'.b')  #plot all the points
  xr = [R[0][0],R[0][0],R[1][0],R[1][0],R[0][0]]  #plot rectangle
  yr = [R[0][1],R[1][1], R[1][1], R[0][1], R[0][1]]
  plt.plot(xr,yr,'-k')
  plt.title('Obstacles and Radar')
  plt.show()

import numpy as np
import matplotlib.pyplot as plt

Points = [(np.random.uniform(0,15),np.random.uniform(0,15)) for i in range(50)]   #obstacles that the robot must avoid
List_points = np.array(Points)
print("List of Obstacles:")
print(List_points)

from search_kd import createKd, searchKd

root = createKd(Points)
infreg = ((-float("inf"),float("inf")),(-float("inf"),float("inf")))  
R = ((6.0,6.0),(10.0,10.0))  
leaves = []
searchKd(root, infreg, R, leaves)
print('Number of obstacles very near the robot: ', len(leaves))
print('Obstacles into the radar:', *leaves, sep = "\n") #points into the rectangle
plotPointsRect(List_points, R)