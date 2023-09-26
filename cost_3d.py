import numpy as np
import matplotlib.pyplot as plt

length = 100
xo = np.linspace(0,10,length)
yo = 3*xo + 8
noise1 = [4.5*(np.random.rand()-0.5) for i in range(length)]
noise2 = [2.5*(np.random.rand()-0.5) for i in range(length)]
y = yo + noise1 + noise2

plt.scatter(xo,y)        #The generated data
# plt.plot(xo, yo, 'r')  #The original line to which noise is added
plt.show()

m = np.linspace(2.8, 3.2, 10)
c = np.linspace(-1000, 1000, 500)
M, C = np.meshgrid(m, c)

cost = np.zeros(np.shape(M))

# cost = M*xo + C - y
for i in xo:
    for j in y:
        cost += (M*i + C - j)**2

fig = plt.figure()
axes = plt.axes(projection = '3d')
axes.plot_surface(M, C, cost)
axes.contour3D(M, C, cost)
plt.show()
