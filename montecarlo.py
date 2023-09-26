import matplotlib.pyplot as plt
import numpy as np

x1 = []
y1 = []
error = []

minSampleSize = 100000
maxSampleSize = 500000
gap = 1000

for size in range(minSampleSize, maxSampleSize, gap):
    x1.append(size)
    ''' Square from -1 < x,y < 1 '''
    x = 2*np.random.rand(size) - 1
    y = 2*np.random.rand(size) - 1

    # plt.scatter(x, y)
    # plt.grid()
    # plt.show()
    i = 0

    ''' Condition for circle x**2 + y**2 = 1'''
    X = x**2
    Y = y**2

    res = X + Y
    res[res < 1] = 1
    res[res > 1] = 0

    '''
    * Ratio should be :
    * Area of circle / Area of square
    * pi(r*r) / (2r)**2
    * pi / 4
    '''
    i += np.sum(res)
    ratio = i/size
    # print("Ratio : ", ratio, " Error : ", ratio - np.pi / 4)
    y1.append(ratio)
    error.append(ratio - np.pi/4)

pi4 = []
for _ in x1:
    pi4.append(np.pi/4)
plt.plot(x1, y1)
plt.plot(x1, error)
plt.plot(x1, pi4)
plt.grid()
plt.show()
print("ANS ORIGINAL : ", np.pi/4)
print("APPROX ANS   : ", np.average(y1), "AVERAGE ERROR : ", np.average(error))
