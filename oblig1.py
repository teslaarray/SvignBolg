import numpy as np
import matplotlib.pyplot as pl

k = 8
m = 2
A = 1.077032961
phi = 1.1902899

omega = 2  # sqrt(4)


def bev(t):
    return A * np.cos(omega * t + phi)


def speedo(t):
    return -A * omega * np.sin(omega * t + phi)


T = 2 * np.pi / omega

t = np.linspace(0, T, 50)
x = bev(t)
v = speedo(t)
p = v * m

pl.plot(x, p)
pl.axis("equal")
pl.xlabel("position (m)")
pl.ylabel("momentum (kg m/s)")
pl.show()
# får en ellipse

# ------------skalering----------------

# skalerer x aksen med maks amplitude av x(t)
# y aksen med ( maks amplitude av v(t) )*massen

xstj = x / A
pstj = p / (A * omega * m)

pl.plot(xstj, pstj)
pl.axis("equal")
pl.xlabel("position")
pl.ylabel("momentum")
pl.show()

# får en sirkel