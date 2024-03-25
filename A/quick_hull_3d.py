from scipy.spatial import ConvexHull

def quickhull3d(P):
  return ConvexHull(P)
     