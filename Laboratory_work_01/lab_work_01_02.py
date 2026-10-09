from math import *

a = float(input('Введите угол alpha: '))
x = float(input('Введите угол beta: '))

y = (cos(a)-cos(x))**2-(sin(a)-sin(x))**2
print("{0:.2f} {1:.2f} {2:.4f}".format(a, x, y))

y = -4*sin((a-x)/2)**2*cos(a+x)
print("{0:.2f} {1:.2f} {2:.4f}".format(a, x, y))

