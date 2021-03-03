def getN(x):
    l = np.sqrt(x ** 2 + h ** 2)
    return k * (l0 - l) * h / l + m * 9.81


miD = 0.05


def doPlots2(x0):

    t = np.linspace(0, 10, 5000)  # tid for å plotte
    v = np.zeros_like(t)  # fart
    x = np.zeros_like(t)  # pos

    x[0] = x0

    # bare en kraft virker på sylinderen

    dt = t[1] - t[0]
    for i in range(len(t) - 1):
        a = Tx(x[i]) / m

        if i > 0:  # fordi funskjonen må vite retningen til bevegelsen

            dx = x[i] - x[i - 1]
            # friksjon virker i motsatt retning til bevegelsen
            a += miD * getN(x[i]) * np.sign(-dx) / m

        v[i + 1] = v[i] + a * dt
        x[i + 1] = x[i] + v[i + 1] * dt

    pl.figure(figsize=(8, 8))

    pl.subplot(211)
    pl.plot(t, v)
    pl.xlabel("tid (s)")
    pl.ylabel("fart (m/s)")

    pl.subplot(212)
    pl.plot(t, x)
    pl.xlabel("tid (s)")
    pl.ylabel("pos (m)")

    pl.show()


doPlots2(0.75)