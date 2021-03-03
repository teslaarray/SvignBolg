import numpy as np
import matplotlib.pyplot as pl


def g(f, t):
    return 1 * np.sin(2 * np.pi * f * t)


def doFreqAn(func, f, fs, T):

    N = int(T * fs)  # tid * hvor mange per tid
    t = np.linspace(0, T, N)
    sampFunc = func(f, t)  # samplingen

    Ck = np.fft.fft(sampFunc) / N  # normalisert fft
    freq = np.fft.fftfreq(N, 1 / fs)
    # freq = np.linspace(0, N - 1, N)

    return Ck, freq, sampFunc, t


# 1a)


def opg1(f, fs):

    Ck, freq, sampFunc, t = doFreqAn(g, f, fs, 1)

    pl.figure(figsize=(6, 6))

    pl.subplot(212)
    pl.plot(freq, np.abs(Ck))
    pl.xlabel("frequency")
    pl.ylabel("abs (Ck)")

    pl.subplot(211)
    pl.plot(t, sampFunc, label=f"f = {f}")
    pl.xlabel("time (s)")
    pl.ylabel("amplitude (m)")
    pl.legend(loc=1)

    pl.show()

    # amplituden er som forventet, 0.5 for pos og neg frekvens = 1


opg1(100, 1000)