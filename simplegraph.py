#import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('TkAgg')
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show(block=True)