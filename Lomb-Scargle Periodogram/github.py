import numpy as np
import matplotlib.pyplot as plt

from astroML.datasets import fetch_LINEAR_sample
from gatspy.periodic import LombScargleFast

LINEAR_data = fetch_LINEAR_sample()
star_id = 10040133
t, mag, dmag = LINEAR_data.get_light_curve(star_id).T

# fig, ax = plt.subplots()
# ax.errorbar(t, mag, dmag, fmt='.k', ecolor='gray')
# ax.set(xlabel='Time (days)', ylabel='magitude',
#        title='LINEAR object {0}'.format(star_id))
# ax.invert_yaxis()
# plt.show()


model = LombScargleFast().fit(t, mag, dmag)
periods, power = model.periodogram_auto(nyquist_factor=100)

fig, ax = plt.subplots()
ax.plot(periods, power)
ax.set(xlim=(0.2, 1.4), ylim=(0, 0.8),
       xlabel='period (days)',
       ylabel='Lomb-Scargle Power')
plt.show()