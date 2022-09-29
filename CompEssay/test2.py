import numpy as np
import matplotlib.pyplot as pl


# def eom(w):
#     return np.exp(1j * w)


# t = np.linspace(0, 2 * np.pi, 1000)


# def Hs(w):
#     return (1 - (-eom(w)) ** -6) / (1 - (-eom(w)) ** -1)


# hes = Hs(t)
# # htest = test(t)

# hesAbs = np.abs(hes)
# hesPhase = np.arctan(np.imag(hes), np.real(hes))

# pl.plot(t, hesAbs, label="ABs")
# pl.plot(t, hesPhase, label="phase")
# # pl.plot(t, np.abs(htest), label="test abs")
# pl.legend()
# pl.show()


k = np.array([0, 1, 2, 3, 4])

y = np.pi / 5 + 2 * np.pi / 5 * k

print(y / np.pi)
