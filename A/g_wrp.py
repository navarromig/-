import numpy as np

def orientation(p1,p2,p3):
  if((p2[0]*p3[1])-(p2[1]*p3[0])-(p1[0]*p3[1])+(p1[1]*p3[0])+(p1[0]*p2[1])-(p1[1]*p2[0])) < 0:    
    return True
  return False

def collinear(p1,p2,p3):
  if((p3[1] - p2[1])*(p2[0] - p1[0]) == (p2[1] - p1[1])*(p3[0] - p2[0])):
    return True
  return False

def giftwrapping(S):
  S = sorted(S, key=lambda k: [k[0],k[1]])        #sort S with the smallest x
  r0 = S[0]                                       #initializing r0
  r = r0                                          #initializing current r
  Points = []                                          #initializing chain of points
  while True:
    Points.append(r)                                   #current point in chain
    u = S[0]                                      #r0 point as u
    for j in range(1,len(S)):
      t = S[j]                                      #point t in S
      if(orientation(r,u,t) or collinear(r,u,t)):   #checking CW orientation and collinear condition
        u = t
    if(u == r0):                                    #end point is the starting point
      break
    r = u
    S.remove(r)                                    #removing visisted point r
  return np.array(Points)
     