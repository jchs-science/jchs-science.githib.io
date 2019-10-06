import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 5.1, 1, )
y = [3 for i in x]

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(4, 4))

ax.plot(x, y, marker='.', ls='-', color='blue')

ax.set_xlim(0, 5)
ax.set_ylim(0, 5)

ax.set_title('Postion vs Time')
ax.set_xlabel('time (s)')
ax.set_ylabel('postion (m)')

ax.grid()

plt.tight_layout()
plt.savefig('1.1-motion-position.png', format='png')

plt.show()
