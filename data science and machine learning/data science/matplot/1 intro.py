import numpy as np
import matplotlib.pyplot as plt

xPoints = np.array([0,6])
print(xPoints)

yPoints = np.array([0,250])
print(yPoints)

# plt.plot(xPoints, yPoints)# with line
# plt.plot(xPoints, yPoints, 'o')# without line
# multiple points
# xPoints = np.array([1,2,3,4,8])
# yPoints = np.array([3,8,1,10,5])
# plt.plot(xPoints, yPoints,marker='o', linestyle='dotted', color='r',ms=10,mec="g",linewidth="5") #line style: solid, dashed, dashdot, dotted

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
plt.plot(y1)
plt.plot(y2)

plt.show()