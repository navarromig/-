import math

def divideConquer(Points):
  Points.sort()                            #sort by x
  if(len(Points) <= 2):                    #condition : not enough points to run the algorith
    return Points
  a_length = math.ceil(len(Points)/2)
  b_length = math.floor(len(Points)/2)
  a = Points[0:a_length]                      
  b = Points[a_length:len(Points)]
  a_hull = divideConquer(a)            #using recursion for the convex hull of the 2 subsets
  b_hull = divideConquer(b)
  return merge_hull(a_hull,b_hull)           #merging convex hulls

def merge_hull(a_hull, b_hull):
  right_most_a = max(a_hull)             #find rightmost point of a
  left_most_b = min(b_hull)              #find leftmost point of b
  upper_a, upper_b, lower_a, lower_b = intersection(a_hull, b_hull, right_most_a, left_most_b)
  mergedch = []                       #merged polygon
  a_i = upper_a
  mergedch.append(a_hull[upper_a])      #begin with upper point of hull A
  while a_i!=lower_a:                   #append all the points between upper and lower point of A - counterclockwise orientation
    a_i = (a_i + 1)%len(a_hull)          #attention to limits
    mergedch.append(a_hull[a_i])

  b_j = lower_b
  mergedch.append(b_hull[lower_b])      #connect the half of convex hull A with the lowest point of B
  while b_j!=upper_b:                   #append all the points between lower and upper point of B - counterclockwise orientation
    b_j = (b_j + 1)%len(b_hull)          #attention to limits
    mergedch.append(b_hull[b_j])

  return mergedch


def orientation(p1,p2,p3):
  if((p2[0]*p3[1])-(p2[1]*p3[0])-(p1[0]*p3[1])+(p1[1]*p3[0])+(p1[0]*p2[1])-(p1[1]*p2[0])) < 0:    #right orientation
    return True
  return False

def collinear(p1,p2,p3):
  if((p3[1] - p2[1])*(p2[0] - p1[0]) == (p2[1] - p1[1])*(p3[0] - p2[0])):
    return True
  return False
  
def intersection(a_hull, b_hull, right_most_a, left_most_b):
  a_i = a_hull.index(right_most_a)        #find a_i
  b_j = b_hull.index(left_most_b)         #find b_j

  a_i1 = a_i
  b_j1 = b_j
  flag = 1
  while flag:
    flag = 0
    a_i2 = (a_i1 + 1) % len(a_hull)                    #a_i+1 - attention not getting out of limits
    while(orientation(a_hull[a_i1],a_hull[a_i2],b_hull[b_j1]) and not collinear(a_hull[a_i1],a_hull[a_i2],b_hull[b_j1])):     #clockwise a_i a_i+1 b_j - case for collinearity
      a_i1 = (a_i1 + 1) % len(a_hull)              #increase i
      a_i2 = (a_i1 + 1) % len(a_hull)
      flag = 1                                    #i changed

    b_j2 = (b_j1 - 1 + len(b_hull))%len(b_hull)        #b_j-1
    while(orientation(b_hull[b_j2],b_hull[b_j1],a_hull[a_i1]) and not collinear(b_hull[b_j2],b_hull[b_j1],a_hull[a_i1])):     #clockwise b_j-1 b_j a_i case for collinearity
      b_j1 = (b_j1 - 1 + len(b_hull))%len(b_hull)
      b_j2 = (b_j1 - 1 + len(b_hull))%len(b_hull)
      flag = 1                                    #j changed

  upper_a = a_i1                          #upper bridge a_i - b_j
  upper_b = b_j1

  a_i1 = a_i
  b_j1 = b_j
  flag = 1
  while flag:
    flag = 0
    b_j2 = (b_j1 + 1) % len(b_hull)                    #Bi+1 - attention not getting out of limits
    while(orientation(b_hull[b_j1],b_hull[b_j2],a_hull[a_i1]) and not collinear(b_hull[b_j1],b_hull[b_j2],a_hull[a_i1])):     #clockwise b_j b_j+1 a_i
      b_j1 = (b_j1 + 1) % len(b_hull)              #increase j
      b_j2 = (b_j1 + 1) % len(b_hull)
      flag = 1                                    #j changed

    a_i2 = (a_i1 - 1 + len(a_hull))%len(a_hull)        #Aj-1
    while(orientation(a_hull[a_i2],a_hull[a_i1],b_hull[b_j1]) and not collinear(a_hull[a_i2],a_hull[a_i1],b_hull[b_j1])):     #clockwise a_i-1 a_i b_j
      a_i1 = (a_i1 - 1 + len(a_hull))%len(a_hull)
      a_i2 = (a_i1 - 1 + len(a_hull))%len(a_hull)
      flag = 1                                    #i changed

  lower_a = a_i1                          #lower bridge a_ib_j
  lower_b = b_j1

  return upper_a, upper_b, lower_a, lower_b