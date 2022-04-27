import matplotlib.pyplot as plt
import numpy as np
import itertools

xs = [0,30,60,100]
fs = [0,50,40,10]

print("input values of d : ")
d = [float(input("d("+str(i)+") : ")) for i in range(len(xs)-1)]

b = xs[3]-xs[0]
a = []
e = []
c = []
f = []
for i in [1,2,3]:
    a.append((xs[i]-xs[i-1])/b)
    e.append( ( xs[3]*xs[i-1] - xs[i]*xs[0] )/b )
    c.append( ( fs[i] - fs[i-1] - d[i-1]*(fs[3]-fs[0]) )/b )
    f.append( ( fs[i-1]*xs[3] - xs[0]*fs[i] - d[i-1]*( xs[3]*fs[0] - xs[0]*fs[3] ) )/b )

prob = [0.33,0.34,0.33]



x = np.linspace(0,1,10000)
y = np.linspace(0,1,10000)

initial = []

for x,y in zip(x,y):
    initial.append([0,y])

initial = np.array(initial)


iters = 1000
fig = plt.figure(figsize=(10,10))

j=0

for i in range(iters):
  temp = []
  
  for x,y in initial:
    rnd = np.random.choice([0,1,2], p=prob)
    nx = a[rnd]*x+e[rnd]
    ny = c[rnd]*x+d[rnd]*y+f[rnd]
    temp.append([nx,ny])

  initial = np.array(temp)
  if (i+1)%100==0:  
    xf,yf = initial[:,0],initial[:,1]
    ax = fig.add_subplot(5,2,j+1)
    ax.scatter(xf,yf,s=1)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_title('iteration '+str(i+1))
    j+=1

plt.show()


x,y = initial[:,0],initial[:,1]
fig = plt.figure(figsize=(10, 6))

plt.scatter(x,y,s=1)
plt.xticks([])
plt.yticks([])
plt.show()