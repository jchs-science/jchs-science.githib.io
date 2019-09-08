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

x = np.arange(0, 5.1, 1, )
y = x

ax.plot(x, y, marker='.', ls='-', color='blue')
ax.set_title('Constant Positive Velocity')

# make the second plot
ax = axes[1]

x = np.arange(0, 5.1, 1, )
y = 5 - x

ax.plot(x, y, marker='.', ls='-', color='red')
ax.set_title('Constant Negative Velocity')


plt.tight_layout()
plt.savefig('1.1-motion-velocity.pdf', format='pdf')

plt.show()
