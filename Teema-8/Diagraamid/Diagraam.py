import matplotlib.pyplot as plt
import numpy as np

x1 = np.arange(-12, 13, 0.5)
y1 = -1/18 * (x1**2) + 12

x2 = np.arange(-4, 5, 0.5)
y2 = -1/8 * (x2**2) + 6

x3 = np.arange(-12, -3, 0.5)
y3 = -1/8 * (x3+8)**2 + 6 

x4 = np.arange(4, 13, 0.5)
y4 = -1/8 * ((x4-8)**2) + 6 

x5 = np.arange(-4, -1.3, 0.5)
y5 = 2 * (x5+3) ** 2 - 9

x6 = np.arange(-4, 1.2, 0.5)
y6 = 1.5 * ( (x6 + 3) ** 2 ) -10 

plt.plot(x1, y1, linestyle='-', marker='o', color='blue', markersize=3, markerfacecolor='lightblue')
plt.plot(x2, y2, linestyle='-', marker='o', color='blue', markersize=3, markerfacecolor='lightblue')
plt.plot(x3, y3, linestyle='-', marker='o', color='blue', markersize=3, markerfacecolor='lightblue')
plt.plot(x4, y4, linestyle='-', marker='o', color='blue', markersize=3, markerfacecolor='lightblue')
plt.plot(x5, y5, linestyle='-', marker='o', color='blue', markersize=3, markerfacecolor='lightblue')
plt.plot(x6, y6, linestyle='-', marker='o', color='blue', markersize=3, markerfacecolor='lightblue')

plt.title("Kahe joone näide")
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.show()
