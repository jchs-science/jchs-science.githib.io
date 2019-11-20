from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.text import Text
import numpy as np

# Sampling rate 1000 hz / second

t = np.linspace(0, 0.99, 1000, endpoint=True)

fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 3))
plt.axis('off')

ax.plot(t, signal.square(2 * np.pi * 5 * t), color='k')
ax.set_title('Threshold of a Digital Signal')

ax.axhline(y=0, color='k', ls='--')

plt.text(0.01, 0.5, 'Yes', color='g')
plt.text(0.01, -0.5, 'No', color='r')

ax.set_ylim(-1.1, 1.1)

plt.tight_layout()
plt.savefig('./digital-threshold.png', format='png', dpi=100)
# plt.show()


# Create a new plot for the frequency consideration
fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 3))
ax.set_frame_on(False)
ax.get_xaxis().tick_bottom()
ax.axes.get_yaxis().set_visible(False)
xmin, xmax = ax.get_xaxis().get_view_interval()
ymin, ymax = ax.get_yaxis().get_view_interval()
ax.add_artist(Line2D((xmin, xmax), (ymin, ymin), color='black', linewidth=2))

ax.set_xlim(0, 1)

ax.set_xlabel('Time in seconds')

ax.plot(t, signal.square(2 * np.pi * 5 * t) + 1.2, color='k')
ax.set_title('Threshold of a Digital Signal')

ax.set_ylim(-0, 2.3)

plt.tight_layout()
plt.savefig('./digital-frequency.png', format='png', dpi=100)
plt.show()
