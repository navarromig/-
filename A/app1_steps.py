import numpy as np

Points = [(np.random.uniform(0,200),np.random.uniform(0,200)) for i in range(100)]
List_points = np.array(Points)
print("List of points:")
print(List_points)

import matplotlib.pyplot as plt
from incr import incremental, orientation

List_points = np.array(Points)
L = incremental(Points)
print("Points of convex hull:")
print(L)
Points.sort()
fig = plt.figure(figsize=(15,20))
ax = fig.add_subplot(431)
List_points = np.array(Points)
plt.plot(List_points[:,0],List_points[:,1],'.b')
plt.title("Points")

ax = fig.add_subplot(432)
Lup = [Points[0],Points[1]]
Lupar = np.array((list(Points[0]),list(Points[1])))
plt.plot(List_points[:,0],List_points[:,1],'.b')
plt.plot(Lupar[:,0],Lupar[:,1],'k-')        #p1 and p2
plt.title("Vertex p1 - p2")

for i in range(2,len(Points)):
  Lup.append(Points[i])
  while(len(Lup) > 2 and not orientation(Lup[len(Lup)-3],Lup[len(Lup)-2],Lup[len(Lup)-1])):
    Lup.pop(len(Lup)-2)

ax = fig.add_subplot(433)
j = 0
Lupar = [list(Lup[j]) for j in range(len(Lup))]
Lupar = np.array(Lupar)
plt.plot(List_points[:,0],List_points[:,1],'.b')
plt.plot(Lupar[:,0],Lupar[:,1],'k-')
plt.title("Vertices of L upper")


ax = fig.add_subplot(434)
Llow  = [Points[len(Points)-1],Points[len(Points)-2]]
Llowar = np.array((list(Points[len(Points)-1]),list(Points[len(Points)-2])))
plt.plot(List_points[:,0],List_points[:,1],'.b')
plt.plot(Llowar[:,0],Llowar[:,1],'k-')        #pn and pn-1
plt.title("Vertex pn - pn-1")

for i in range(len(Points)-3,-1,-1):
  Llow.append(Points[i])
  while(len(Llow) > 2 and not orientation(Llow[len(Llow)-3],Llow[len(Llow)-2],Llow[len(Llow)-1])):
    Llow.pop(len(Llow)-2)

ax = fig.add_subplot(435)
j = 0
Llowar = [list(Llow[j]) for j in range(len(Llow))]
Llowar = np.array(Llowar)
plt.plot(List_points[:,0],List_points[:,1],'.b')
plt.plot(Llowar[:,0],Llowar[:,1],'k-')
plt.title("Vertices of L low")

Llow.pop(0)
Llow.pop(len(Llow)-1)

ax = fig.add_subplot(436)
j = 0
Llowar = [list(Llow[j]) for j in range(len(Llow))]
Llowar = np.array(Llowar)
plt.plot(List_points[:,0],List_points[:,1],'.b')
plt.plot(Llowar[:,0],Llowar[:,1],'k-')
plt.title("Vertices of L low without p1, pn")

L = Lup + Llow

ax = fig.add_subplot(437)
j = 0
Lar = [list(L[j]) for j in range(len(L))]
Lar = np.array(Lar)
plt.plot(List_points[:,0],List_points[:,1],'.b')
plt.plot(Lar[:,0],Lar[:,1],'k-')
plt.title("Lup + Low")


ax = fig.add_subplot(438)
plt.plot(List_points[:,0],List_points[:,1],'.b')
x = Lar[:,0]
y = Lar[:,1]
plt.plot(x,y,'k-')
xlast = [Lar[len(x)-1,0],Lar[0,0]]
ylast = [Lar[len(x)-1,1],Lar[0,1]]
plt.plot(xlast, ylast, 'k-')    #plot last vertex
plt.title("Convex hull")
fig.tight_layout(pad=7.0)
plt.show()