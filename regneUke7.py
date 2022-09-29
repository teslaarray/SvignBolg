import numpy as np
import matplotlib.pyplot as pl
from matplotlib.animation import FuncAnimation

N = 30

k = 200  # N/m
m = 5  # kg

L0 = 1  # m
T = 20  # s
J = int(T * 1000)

X = np.zeros((J, N), dtype=float)
A = np.zeros_like(X)
V = np.zeros_like(X)

X[0, :] = np.array([i * L0 for i in range(N)])
Const = [0, N - 1]  # not to be moved
Yplot = np.zeros(N)

t = np.linspace(0, T, J)
dt = t[1] - t[0]
# set init bet
X[0, 1] -= 0.5
# --------


def getFi(j, i):
    j = j - 1
    if i == 0:
        return -k * (L0 - (X[j, i + 1] - X[j, i]))
    if i == (N - 1):
        return k * (L0 - (X[j, i] - X[j, i - 1]))
    else:
        return -k * (L0 - (X[j, i + 1] - X[j, i])) + k * (L0 - (X[j, i] - X[j, i - 1]))


for j in range(J - 1):

    for i in range(N):
        if i in Const:
            X[j + 1, i] = X[j, i]
        else:
            fi = getFi(j, i)
            A[j + 1, i] = fi / m
            V[j + 1, i] = V[j, i] + dt * A[j, i]
            X[j + 1, i] = X[j, i] + dt * V[j + 1, i]


fig = pl.figure()
ax = pl.axes()

line = ax.scatter(X[0, :], Yplot)
ax.axis([-1, L0 * N + 1, -1, 1])


def initLine():
    return (line,)


fps = 50


def updateAni(l):
    data = np.zeros((N, 2))
    data[:, 0] = X[l * fps, :]
    data[:, 1] = Yplot[:]

    line.set_offsets(data)
    return (line,)


doAni = FuncAnimation(
    fig,
    updateAni,
    init_func=initLine,
    frames=int(J / fps),
    interval=int(1 / fps * 1000),
    blit=True,
)

pl.show()