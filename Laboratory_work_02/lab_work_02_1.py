from math import sqrt

x = float(input("Введите значение X = "))
y = 0.0

if -7 <= x < -3:
    y = x + 7
elif -3 <= x < -2:
    y = 4
elif -2 <= x <= 2:
    y = x**2
elif 2 < x <= 4:
    y = 8 - 2*x
else:
    y = None

if y is None:
    print("X вне области определения [-7, 4]")
else:
    print("X = {0:.2f} Y = {1:.2f}".format(x, y))
