from matplotlib.lines import lineStyles
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0, 10, 1) #0-9
y=x**2-5*x+6
plt.figure(facecolor='lightblue')
plt.title("Parabola")
plt.xlabel("x telg")
plt.ylabel("y telg")
plt.grid(True)

plt.plot(x,y, color='blue', linestyle='-', marker='D', markersize=8,label="joonise")
