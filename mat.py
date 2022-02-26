import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-np.pi,np.pi,100)

# the functions, which are y = sin(x) and z = cos(x) here
y = np.sin(x)
z = np.cos(x)

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
#grid
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')

# plot the functions
plt.plot(x,y, 'c', label='y=sin(x)')
plt.plot(x,z, 'm', label='y=cos(x)')

#plt.legend(loc='upper left')

# show the plot
plt.show()
