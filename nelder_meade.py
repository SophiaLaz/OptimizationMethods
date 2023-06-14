import numpy as np


def f0(x, coef):
    return 4 * (x[0] - coef[0]) ** 2 + (x[1] - coef[1]) ** 2


def f1(x, coef):
    return (x[0]-coef[0])**2 + x[0]*x[1] + coef[1]*(x[1]-3)**2


def Nealder_Mead(f, x0, tol, coef):
    al = 1
    beta = 0.5
    gam = 2
    flag = True
    while flag:
        i_l, i_s, i_h = np.argsort([f(xi, coef) for xi in x0])
        x_l, x_s, x_h = x0[i_l], x0[i_s], x0[i_h]

        x_2 = (x_l + x_s) / 2

        sigma = (sum([(f(x0[i], coef) - f(x_2, coef)) ** 2 for i in range(3)]) / 3) ** (1 / 2)

        if sigma <= tol:
            flag = False
            return f(x_l, coef)
        else:
            x_3 = x_2 + al * (x_2 - x_h)

            if f(x_3, coef) <= f(x_l, coef):
                x_4 = x_2 + gam * (x_3 - x_2)
                if f(x_4, coef) < f(x_l, coef):
                    x0[i_h] = x_4
                elif f(x_4, coef) >= f(x_l, coef):
                    x0[i_h] = x_3
                elif f(x_4, coef) >= f(x_l, coef):
                    x0[i_h] = x_3

            elif (f(x_3, coef) <= f(x_h, coef)) and (f(x_3, coef) > f(x_s, coef)):
                x_5 = x_2 + beta * (x_h - x_2)
                x0[i_h] = x_5

            elif (f(x_3, coef) <= f(x_s, coef)) and (f(x_3, coef) > f(x_l, coef)):
                x0[i_h] = x_3

            elif f(x_3, coef) > f(x_h, coef):
                for i in range(3):
                    x0[i] = x_l + 0.5 * (x0[i] - x_l)


if __name__ == '__main__':
    type = int(input())
    f = f0 if (type == 0) else f1
    coef = [i for i in map(float,input().split())]
    x0 = []
    for k in range(3):
        x0.append(np.array([i for i in map(float,input().split())]))
    tol = float(input())
    r1 = Nealder_Mead(f, x0, tol, coef)
    print("{:.10f}".format(r1))
