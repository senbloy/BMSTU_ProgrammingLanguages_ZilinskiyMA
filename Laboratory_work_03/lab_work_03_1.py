from math import *

xb = float(input('Введите Xbeg='))
xe = float(input('Введите Xend='))
dx = float(input('Введите Dx='))
if dx <= 0:
    raise ValueError("Dx должен быть положительным")
print("Xbeg={0: 7.2f} Xend={1: 7.2f}".format(xb, xe))
print(" Dx={0: 7.2f}".format(dx))
xt = xb
print("+--------+--------+")
print("I X I Y I")
print("+--------+--------+")
while xt <= xe:
    if -7 <= xt < -3:
        y = xt + 7
    elif -3 <= xt < -2:
        y = 4
    elif -2 <= xt <= 2:
        y = xt**2
    elif 2 < xt <= 4:
        y = 8 - 2*xt
    else:
        y = None
    if y is None:
        print("X вне области определения [-7, 4]")
        xt += dx
        continue
    print("I{0: 7.2f} I{1: 7.2f} I".format(xt, y))
    xt += dx
print("+--------+--------+")
