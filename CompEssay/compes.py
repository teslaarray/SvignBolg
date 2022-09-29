import numpy as np
import matplotlib.pyplot as pl
import matplotlib.animation as animation

eps_0 = 8.854e-12
mu_0 = 1.256e-6
forPie = 4 * np.pi
k = 200000

# the boundaries

# 3 meters in the negative and positive direction
xlim = 3
ylim = 3

# table surface z coord, unlimited in pos z-direction
zlim = 0


class Ball:
    def __init__(self, x, y, c, R, m, V):

        """
        x, y, z = position
        c = charge
        R = radius of the ball
        m = mass

        """

        self.P = np.array([x, y, R])  # z = radius

        self.R = R
        self.c = c
        self.m = m

        # velocity
        self.V = V

        # current total force acting on the ball
        # will be reset after each loop
        self.F = np.zeros(3)


balls = []


def getColF(b1, b2):

    dist = np.linalg.norm(b1.P - b2.P)

    return 2000000 * dist - 0.2 * (b1.V - b2.V)


def calcEf():

    """
    calculates the forces on all the balls
    that come from the electric field

    """
    n = len(balls)

    for i in range(n - 1):

        for j in range(i + 1, n):

            # F = force from j on i,
            # then the force from i on j is -F
            # so there is no need to calculate it twice

            r = balls[i].P - balls[j].P
            norm = np.linalg.norm(r) ** 3
            F = balls[i].c * balls[j].c * r / (forPie * eps_0 * norm)
            balls[i].F += F
            balls[j].F -= F


def calcBf():

    """
    calculates the forces on all the balls
    that come from the magnetic fields

    """

    # since the magnetic field is made of magic and doesnt follow N3L
    # it needs to be calculated from (every ball) on (every ball)

    # from
    for b1 in balls:

        # to
        for b2 in balls:
            if b1 != b2:

                r = b2.P - b1.P
                B = mu_0 / forPie * (np.cross(b1.c * b1.V, r)) / np.linalg.norm(r) ** 3
                b2.F += np.cross(b2.c * b2.V, B)

    B = np.zeros(3)


# ball on ball collision force


def calcColF():

    N = len(balls)

    for i in range(N - 1):
        for j in range(i + 1, N):

            # F = force from j on i,
            # then the force from i on j is -F
            # so there is no need to calculate it twice

            if balls[i].P[2] > 1:
                l = 0

            if balls[j].P[2] > 1:
                p = 0

            r = balls[i].P - balls[j].P
            rnorm = np.linalg.norm(r)
            dist = balls[i].R + balls[j].R

            if rnorm < dist:  # if they are touching

                F = k * (dist - rnorm) * r / rnorm

                balls[i].F += F  # ball i gets hit in the direction of r
                balls[j].F -= F  # ball j in the opposite direction


# table collisions, four walls and table surface


def calcTableF():

    for b in balls:

        P = b.P

        # check x-coord limits
        if P[0] - b.R < -xlim:

            # distance between ball surface and table wall
            dist = abs(P[0] - b.R + xlim)
            b.F += k * dist * np.array([1, 0, 0])  # in the positive x-direction
        else:
            if P[0] + b.R > xlim:

                dist = abs(P[0] + b.R - xlim)
                b.F += k * dist * np.array([-1, 0, 0])

        # check y-coord limits
        if P[1] - b.R < -ylim:

            dist = abs(P[1] - b.R + ylim)
            b.F += k * dist * np.array([0, 1, 0])
        else:
            if P[1] + b.R > ylim:

                dist = abs(P[1] + b.R - ylim)
                b.F += k * dist * np.array([0, -1, 0])

        # check z-coord limits
        if P[2] - b.R < -zlim:

            dist = abs(P[2] - b.R + zlim)
            b.F += k * dist * np.array([0, 0, 1])


def calcFrictionF():

    # friction = 30% of current velocity
    j = 0.3

    for b in balls:
        b.F += -(j * b.V)


fig = pl.figure()
ax = pl.axes(xlim=(-xlim - 2, xlim + 2), ylim=(-ylim - 2, ylim + 2))
ax.axis("equal")
art = []

radius = 0.4  # of a ball
charge = 0

balls.append(Ball(1, 0, charge, radius, 1, np.array([-8, 0, 0])))
balls.append(Ball(-2, 0, charge, radius, 2, np.array([8, 0, 0])))
balls.append(Ball(0, 2, charge, radius, 1, np.array([4, 4, 0])))
balls.append(Ball(2, 0, charge, radius, 2, np.array([-4, 4, 0])))


def setupBalls():

    for b in balls:
        a = pl.Circle((b.P[0], b.P[1]), b.R)
        ax.add_artist(a)
        art.append(a)
    return art


T = 3
dt = 0.001

N = int(T / dt)


def calculateAll(i):

    # reset the forces
    for b in balls:
        b.F = np.zeros(3)

    # calculate all the forces
    calcEf()  # electric
    calcBf()  # magnetic
    calcColF()  # collision with balls
    calcTableF()  # collision with table
    calcFrictionF()

    for j in range(len(balls)):  # using euler-cromer
        b = balls[j]
        b.V = b.V + dt * b.F / b.m
        b.P = b.P + dt * b.V

        art[j].center = b.P

    return art


def animArt():

    fps = 50

    # make boundaries

    nN = 100

    xlimA = np.linspace(-xlim, xlim, nN)
    ylimA = np.linspace(-ylim, ylim, nN)

    pl.plot(xlimA, [-ylim] * nN, "r")
    pl.plot(xlimA, [ylim] * nN, "r")

    pl.plot([-xlim] * nN, ylimA, "r")
    pl.plot([xlim] * nN, ylimA, "r")

    anim = animation.FuncAnimation(
        fig, calculateAll, frames=N, init_func=setupBalls, interval=5, blit=False
    )
    pl.show()


animArt()