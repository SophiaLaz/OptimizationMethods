import numpy as np


def f0(x, coef):
    return coef[0]*x[0]**4 + coef[1]*x[1]**3 + coef[2]*x[1]**2 + coef[3]*x[0] + coef[4]


def f1(x, coef):
    return x[0]**2 + coef[0]*x[0]*x[1] + coef[1]*(x[1]-3)**2


def Hooke_Jeeves(f, x0, tol, coef):
    delta = np.array([1.0, 1.0])
    al = 2
    lam = 1
    y = x0
    flag = True
    while flag:
        for i in range(x0.shape[0]):
            y1 = y.copy()
            y1[i] += delta[i]
            y2 = y.copy()
            y2[i] -= delta[i]
            if f(y1, coef) < f(y, coef):
                y = y1
            elif f(y2, coef) < f(y, coef):
                y = y2
        if f(y, coef) < f(x0, coef):
            y_new = y + lam * (y - x0)
            x0 = y
            y = y_new
        else:
            flag = False
            for i in range(delta.shape[0]):
                if delta[i] >= tol:
                    delta[i] /= al
                    flag = True
            y = x0
            if not flag:
                break
    return x0


if __name__ == '__main__':
    type = int(input())
    f = f0 if (type == 0) else f1
    coef = [i for i in map(float, input().split())]
    x0 = np.array([i for i in map(float, input().split())])
    tol = float(input())
    r1 = Hooke_Jeeves(f, x0, tol, coef)
    print("{:.10f} {:.10f}".format(r1[0], r1[1]))
