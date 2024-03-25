import numpy as np

def orientation(p1,p2,p3):
  if((p2[0]*p3[1])-(p2[1]*p3[0])-(p1[0]*p3[1])+(p1[1]*p3[0])+(p1[0]*p2[1])-(p1[1]*p2[0])) < 0:    #right orientation
    return True
  return False

def incremental(Points):
  Points.sort()                                                                                  #sort set by x
  Lup = [Points[0],Points[1]]                                                                         #initializing L upper
  for i in range(2,len(Points)):
    Lup.append(Points[i])
    while(len(Lup) > 2 and not orientation(Lup[len(Lup)-3],Lup[len(Lup)-2],Lup[len(Lup)-1])):   #condition : L upper has more than 2 elements and the 3 last points are not clockwise oriented
      Lup.pop(len(Lup)-2)                                                                     #second from end point is removed
  Llow  = [Points[len(Points)-1],Points[len(Points)-2]]                                                             #initializing L lower
  for i in range(len(Points)-3,-1,-1):
    Llow.append(Points[i])
    while(len(Llow) > 2 and not orientation(Llow[len(Llow)-3],Llow[len(Llow)-2],Llow[len(Llow)-1])):   #condition : L lower has more than 2 elements and the 3 last points are not clockwise oriented
      Llow.pop(len(Llow)-2)                                                                   #rsecond from end point is removed
  Llow.pop(0)                                                                                   #first and last point from L lower are removed
  Llow.pop(len(Llow)-1)
  L = Lup + Llow
  return np.array(L)