import numpy as np
import matplotlib.pyplot as pl
from scipy.signal import lfilter


a1 = [1, 2, 3, 4, 5]
h1 = [0, 0, 0, 1]

a2 = [1, 2, 3, 4, 5]
h2 = [0, 1, 0]

a3 = [1, 2, 3, 4, 5, 6]
h3 = [0, 1]

a4 = [1, 2, 3, 4, 5, 6]
h4 = [0, 1, 0]


c1 = np.convolve(a1, h1, mode="same")
c2 = np.convolve(a2, h2, mode="same")
c3 = np.convolve(a3, h3, mode="same")
c4 = np.convolve(a4, h4, mode="same")

print(c1, c2, c3, c4)