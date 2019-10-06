import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

# setup both plots
for ax in axes:
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)

    ax.set_xlabel('time (s)')
    ax.set_ylabel('postion (m)')

    ax.grid()

# setup the first plot
ax = axes[0]

x = np.arange(0, 5.1, 0.01, )
y = (x - 2.5)**2

ax.plot(x, y, marker='', ls='-', color='blue')
ax.set_title('Positive Acceleration')

# make the second plot
ax = axes[1]

x = np.arange(0, 5.1, 0.01, )
y = -(x - 2.5)**2 + 5

ax.plot(x, y, marker='', ls='-', color='red')
ax.set_title('Negative Acceleration')


plt.tight_layout()
plt.savefig('1.1-motion-acceleration.png', format='png')

plt.show()
