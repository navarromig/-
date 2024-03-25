from scipy.spatial import ConvexHull, convex_hull_plot_2d

def quickhull(P):
  return ConvexHull(P)
