from math import *
from random import *

r = float(input("R="))
if r <= 0:
    raise ValueError("R должен быть положительным")

flag = False
print(" X Y Res")
print("-------------------")
for n in range(10):
    x = uniform(-r, r)
    y = uniform(-r, r)
    if (x*x+y*y <= r*r) and ((x <= 0 and y <= 0) or (x >= 0 and y >= (x-1)**2)):
        flag = True
    else:
        flag = False
    print("{0: 7.2f} {1: 7.2f}".format(x, y), end=' ')
    if flag:
        print("Yes")
    else:
        print("No")
