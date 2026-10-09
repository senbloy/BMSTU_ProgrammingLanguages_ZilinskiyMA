from math import *

print('Введите Xbeg, Xend, Dx и Eps')
xb = float(input('Xbeg='))
xe = float(input('Xend='))
dx = float(input('Dx='))
eps = float(input('Eps='))
if dx <= 0 or eps <= 0 or not -1 <= xb <= xe <= 1:
    raise ValueError("Требуются Dx > 0, Eps > 0 и -1 <= Xbeg <= Xend <= 1")
print("+--------+--------+-----+")
print("I X I Y I N I")
print("+--------+--------+-----+")
xt = xb

while xt <= xe:
    an = xt
    n = 0
    y = an
    while True:
        k = -(xt ** 2) * (2 * n + 1) / (2 * n + 3)
        an = an * k
        y = y + an
        n = n + 1
        if abs(an) < eps:
            break
    print("I{0: 7.2f} I{1: 7.3f} I{2: 4} I".format(xt, y, n + 1))
    xt = xt + dx

print("+--------+--------+-----+")
