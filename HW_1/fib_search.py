def f0(x, coef):
    return coef[0]*x**2 + coef[1]*x + coef[2]


def f1(x, coef):
    return coef[0]*x**4 + coef[1]*x**3 + coef[2]*x**2 + coef[3]*x + coef[4]


def fib(n):
    if n in [0, 1]:
        return 1
    return fib(n - 1) + fib(n - 2)

def fib_search(f, bounds, tol, coef, max_eps=0.01):
    n = 0
    while fib(n) <= ((bounds[1] - bounds[0]) / tol):
        n += 1
    N = n + 1

    c = (bounds[1] - bounds[0]) / fib(N)
    y_0 = bounds[0] + fib(N - 2) * c
    z_0 = bounds[0] + fib(N - 1) * c

    for i in range(2, N - 2):
        if f(z_0, coef) < f(y_0, coef):
            bounds[0] = y_0
            y_0 = z_0
            z_0 = bounds[0] + fib(N - i - 2) / fib(N - i - 1) * (bounds[1] - bounds[0])
        else:
            bounds[1] = z_0
            z_0 = y_0
            y_0 = bounds[0] + fib(N - i - 3) / fib(N - i - 1) * (bounds[1] - bounds[0])

    z_0 = y_0 + max_eps
    if f(z_0, coef) < f(y_0, coef):
        bounds[0] = y_0
    else:
        bounds[1] = z_0

    return (bounds[0] + bounds[1]) / 2


if __name__ == '__main__':
    type = int(input())
    f = f0 if (type == 0) else f1
    coef = [i for i in map(float, input().split())]
    bounds = [0, 0]
    bounds[0], bounds[1], tol = map(float, input().split())
    r1 = fib_search(f, bounds, tol, coef)
    print("{:.10f}".format(r1))
