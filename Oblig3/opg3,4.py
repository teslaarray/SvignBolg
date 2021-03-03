import numpy as np
import matplotlib.pyplot as pl


def doFreqAn2(func, fs=1000, T=1):

    N = int(T * fs)  # tid * hvor mange per tid
    t = np.linspace(0, T, N)
    sampFunc = func(t)  # samplingen

    Ck = np.fft.fft(sampFunc) / N  # normalisert fft
    freq = np.fft.fftfreq(N, 1 / fs)

    return t, sampFunc, Ck, freq


def f(t):
    return 1 * np.sin(2 * np.pi * 100 * t) * np.exp(
        -(((t - 0.2) / 0.05) ** 2)
    ) + 1.7 * np.sin(2 * np.pi * 160 * t) * np.exp(-(((t - 0.6) / 0.1) ** 2))


def opg2a():

    t, sampFunc, Ck, freq = doFreqAn2(f)

    pl.figure(figsize=(13, 7))

    pl.subplot(212)
    pl.plot(freq, np.abs(Ck))
    pl.xlabel("frequency")
    pl.ylabel("abs (Ck)")

    pl.subplot(211)
    pl.plot(t, sampFunc, label="samplede tidsserie")
    pl.xlabel("time (s)")
    pl.ylabel("amplitude (m)")
    pl.legend(loc=1)

    pl.show()


# opg2a()

T = 0.1
fs = 1000
N = int(T * fs)


def wavelet(oma, K, tn, tk):

    C = 0.798 * oma / (fs * K)

    return (C * np.exp(1j * oma * (tn - tk)) - np.exp(-(K ** 2))) * np.exp(
        -(oma ** 2) * ((tn - tk) ** 2) / ((2 * K) ** 2)
    )


def waveletTransform(oma, K):

    t = np.linspace(0, T, N)
    fSamp = f(t)

    line = np.zeros(N, dtype=complex)

    for k in range(N):

        for n in range(N):
            line[k] += fSamp[n] * wavelet(oma, K, t[n], t[k])

    return line


def waveletDiagram(omaArr, K):

    diag = np.zeros((len(omaArr), N), dtype=complex)
    # diag[a, :] = waveletTransformen for alle t-er for vinkelhastighet a

    for i in range(len(omaArr)):
        diag[i] = waveletTransform(omaArr[i], K)

    return diag


def opg3():

    freq = np.linspace(80, 200, 100)
    diag = waveletDiagram(2 * np.pi * freq, 6)

    t = np.linspace(0, T, N)
    print("a")

    t, freq = np.meshgrid(t, freq)

    pl.figure(figsize=(13, 7))
    pl.pcolormesh(t, freq, np.abs(diag))
    pl.xlabel("time (s)")
    pl.ylabel("frekvens (Hz)")
    pl.title("lol")
    pl.legend()

    pl.show()


from scipy.io import wavfile


def opg4():

    fs, data = wavfile.read(
        "C:/Users/DaPC/Documents/GitHub/SvignBolg/Oblig3/attache/cuckoo.wav"
    )
    fsamp = data[:, 0]  # select one out of two channels
    N = data.shape[0]  # number of samples
    T = N / fs

    Ck = (1 / N) * np.fft.fft(fsamp)
    freq = np.fft.fftfreq(N, T / N)

    pl.plot(freq, np.abs(Ck))
    pl.xlabel("frequency (Hz)")
    pl.ylabel("abs (Ck)")
    pl.xlim([-1000, 1000])
    pl.show()

    fsamp = fsamp[int(0.4 * fs) : int(1.1 * fs) : int(np.floor(44.1 / 1.5))]
    N = len(fsamp)
    T = 0.7
    fs = N / T

    Ck = (1 / N) * np.fft.fft(fsamp)
    freq = np.fft.fftfreq(N, T / N)

    pl.plot(freq, np.abs(Ck))
    pl.xlabel("frequency (Hz)")
    pl.ylabel("abs (Ck)")
    pl.show()


opg4()

# c)

# cutting up the data

# play it safe and say we want frequencies up to 750Hz, x2 = 1500 sampling freq
# original is 44.1kHz, so we can pick out every 44.1k/1.5k sample
