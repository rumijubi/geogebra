import matplotlib.pyplot as plt
import numpy as np
x_start=-1
x_end=7
y_start=3
y_end=-2
plt.plot([x_start,x_end],[y_start,y_end])
plt.grid()
axes=plt.gca()
axes.set_aspect(1)
plt.show()
