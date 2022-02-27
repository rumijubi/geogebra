import matplotlib.pyplot as plt
import numpy as np
#color
gr="#C0C0C0"

# 100 linearly spaced numbers
x = np.linspace(-np.pi,np.pi,100)

# the functions, which are y = sin(x) and z = cos(x) here
y = np.sin(x)
z = np.cos(x)

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')

#y_axis color
ax.spines['left'].set_color('red')

ax.spines['bottom'].set_position('center')

#x_axis color
ax.spines['bottom'].set_color('green')

ax.spines['right'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#grid
ax.yaxis.grid(color='gainsboro', linestyle='dashed')
ax.xaxis.grid(color='gainsboro', linestyle='dashed')

# plot the functions
plt.plot(x,y, 'c', label='y=sin(x)')
plt.plot(x,z, 'm', label='y=cos(x)')
#plt.legend(loc='upper left')

# show the plot
plt.show()
