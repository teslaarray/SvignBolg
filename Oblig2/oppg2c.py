import numpy as np
import matplotlib.pyplot as pl

memLen = 30e-3
celleLen = memLen / 3000


def br(l):
    return 0.1e-3 + (0.2e-3 / memLen) * l


def hy(l):
    return 0.3e-3 - (0.2e-3 / memLen) * l


def kf(l):
    return 1e-6 + ((0.1 - 1e-6) / memLen) * l


def rho(l):
    return 1500 + (1000 / memLen) * l


def m(l):
    return br(l) * hy(l) * celleLen * rho(l)


def oscif(l):
    return np.sqrt(kf(l) / m(l))


l = np.linspace(0, memLen, 3000)
omega0 = oscif(l)
pl.plot(l, omega0)
pl.show()


M = m(l)
c4 = 261.63
c4sh = 277.18


def getA(omf, b=0):
    return ((np.sqrt((omega0 ** 2 - omf ** 2) ** 2 + (b * omf / M) ** 2)) * M) ** -1


B = 0.00000001

Ac4 = getA(2 * np.pi * c4, b=B)
Ac4sh = getA(2 * np.pi * c4sh, b=B)

N = 100
# pl.plot(l, Ac4, label="c4 amp resp")
# pl.plot(l, Ac4sh, label="c4sh amp resp")
pl.plot(l[0:N], Ac4[0:N], label="c4 amp resp")
pl.plot(l[0:N], Ac4sh[0:N], label="c4sh amp resp")
pl.legend()
pl.show()
