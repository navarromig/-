import math

class Kdnode:             #class for a kdtree node
  def __init__(self,v):
    self.v = v
    self.vleft = None
    self.vright = None

def createKd(N,depth=0):

  if (len(N) == 0):
    return None

  if (len(N) == 1):
    return Kdnode(N[0])         #single leaf

  elif (len(N) > 1):

    if(depth % 2 != 0):            
      mode = "horizontal"                   #odd
      N.sort(key=lambda x: x[1])
    else:
      mode = "vertical"                     #even
      N.sort(key=lambda x: x[0])

    l = math.ceil(len(N)/2)
    node = Kdnode((N[l], mode))             #store line and mode
    node.vleft = createKd(N[:l],depth+1)
    node.vright = createKd(N[l:],depth+1)

    return node


def reportSubtree(root:Kdnode, leaves):

  if (root == None):
    return

  reportSubtree(root.vleft,leaves)

  if(root.vleft == None and root.vright == None):     #root is leaf
    leaves.append(root.v)

  reportSubtree(root.vright, leaves)


def searchKd(node: Kdnode, curR, R, leaves):

  if (node == None):
    return

  if (node.vleft == None and node.vright == None):   #leaf
    if (R[0][0] <= node.v[0] <= R[1][0] and R[0][1] <= node.v[1] <= R[1][1]):   #R contains leaf
      leaves.append(node.v)
    return

  left_area, right_area = None, None    # when mode = horizontal : left_area == down_area and right_area == up_area

  if(node.v[1] == "horizontal"):
    left_area = ((curR[0][0],curR[0][1]),(curR[1][0],node.v[0][1]))     #set ymax
    right_area = ((curR[0][0],curR[0][1]),(node.v[0][1],curR[1][1]))    #set ymin
  elif(node.v[1] == "vertical"):
    left_area = ((curR[0][0],node.v[0][0]),(curR[1][0],curR[1][1]))     #set xmax
    right_area = ((node.v[0][0],curR[0][1]),(curR[1][0],curR[1][1]))    #set xmin

  if R[0][0] <= left_area[0][0] and R[0][1] <= left_area[1][0] and R[1][0] >= left_area[0][1] and R[1][1] >= left_area[1][1]: #R contains the whole left region
    reportSubtree(node.vleft,leaves)
  elif not(R[0][0] > left_area[0][1] or R[1][0] < left_area[0][0] or R[0][1] > left_area[1][1] or R[1][1] < left_area[1][0]):     #R intersects with left region
    searchKd(node.vleft, left_area, R, leaves)

  if R[0][0] <= right_area[0][0] and R[0][1] <= right_area[1][0] and R[1][0] >= right_area[0][1] and R[1][1] >= right_area[1][1]: #R contains the whole right region
    reportSubtree(node.vright,leaves)
  elif not(R[0][0] > right_area[0][1] or R[1][0] < right_area[0][0] or R[0][1] > right_area[1][1] or R[1][1] < right_area[1][0]):     #R intersects with right region
    searchKd(node.vright, right_area, R, leaves)
