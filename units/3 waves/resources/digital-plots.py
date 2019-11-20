from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.text import Text
import numpy as np

# Sampling rate 1000 hz / second

t = np.linspace(0, 0.99, 1000, endpoint=True)

fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 3))


ax.plot(t, signal.square(2 * np.pi * 5 * t) + 1.1, color='k')
ax.set_title('Threshold of a Digital Signal')

ax.axhline(y=1.1, color='k', ls='--')

plt.text(0.01, 1.5, 'ON', color='g')
plt.text(0.01, 0.5, 'OFF', color='r')

plt.text(0.5, 1.1, 'Threshold line', color='k',
         verticalalignment='center',
         horizontalalignment='center',
         backgroundcolor='white')

ax.fill_between(t, 1.1, 2.2, color='g', alpha=0.2)
ax.fill_between(t, 0, 1.1, color='r', alpha=0.2)

ax.set_ylim(0, 2.2)

ax.set_frame_on(False)
ax.get_xaxis().tick_bottom()
# ax.axes.get_yaxis().set_visible(False)
xmin, xmax = ax.get_xaxis().get_view_interval()
ymin, ymax = ax.get_yaxis().get_view_interval()
ax.add_artist(Line2D((xmin, xmax), (ymin, ymin), color='black', linewidth=2))

ax.set_xlim(0, 1)

ax.set_xlabel('Time in seconds')
ax.set_ylabel('Amplitude')


plt.tight_layout()
plt.savefig('./digital-threshold.png', format='png', dpi=100)
# plt.close()
plt.show()


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
plt.close()


# Absorption
fig, axes = plt.subplots(ncols=2, nrows=1, figsize=(12, 3))
for ax in axes:
    ax.set_ylim(-1, 1)
    ax.set_xlim(0, 1)
    ax.set_xlabel('Time in seconds')
    ax.grid()

ax1, ax2 = axes
ax1.set_title('Wave before absorption')
ax1.plot(t, np.sin(2 * np.pi * 5 * t), color='k')

ax2.set_title('Wave after absorption')

plt.tight_layout()
plt.savefig('./digital-absorbed-blank.png', format='png', dpi=100)
plt.close()

# Absorption-Shown
fig, axes = plt.subplots(ncols=2, nrows=1, figsize=(12, 3))
for ax in axes:
    ax.set_ylim(-1, 1)
    ax.set_xlim(0, 1)
    ax.set_xlabel('Time in seconds')
    ax.grid()

ax1, ax2 = axes
ax1.set_title('Wave before absorption')
ax1.plot(t, np.sin(2 * np.pi * 5 * t), color='k')

ax2.set_title('Wave after absorption')
ax2.plot(t, 0.1 * np.sin(2 * np.pi * 5 * t), color='k')

plt.tight_layout()
plt.savefig('./digital-absorbed-filled.png', format='png', dpi=100)
plt.close()
