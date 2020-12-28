import matplotlib.pyplot as plt
import numpy as np

xdata = np.arange(600, 2501, 1)
ydata = 5 - (xdata - 600) * 4 / (2500 - 600)


fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))

ax.plot(xdata, ydata)
ax.set_ylim(1, 5)
ax.set_xlim(600, 2500)
ax.grid()

ax.set_title('Absorption of a Cell Signal Based on Frequency')
ax.set_xlabel('Frequency of Cell Phone in MHz')
ax.set_ylabel('Number of walls that the cell signal will travel through.')

plt.tight_layout()
plt.savefig('./assessment-absorption.png', format='png', dpi=100)


fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6))

ydata = 20 + 80 * (xdata - 600) / (2500 - 600)

ax.plot(xdata, ydata)
ax.set_ylim(0, 100)
ax.set_xlim(600, 2500)
ax.grid()

ax.set_title('Bandwidth of a Cell Signal Based on Frequency')
ax.set_xlabel('Frequency of Cell Phone in MHz')
ax.set_ylabel('Bandwidth of the Signal in MegaBytes per Second (MB/s)')

plt.tight_layout()
plt.savefig('./assessment-bandwidth.png', format='png', dpi=100)
