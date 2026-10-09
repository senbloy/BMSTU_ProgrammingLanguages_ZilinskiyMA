r = float(input("R="))
if r <= 0:
    raise ValueError("R должен быть положительным")

flag = False
print('Введите координаты X и Y для точки:')
x = float(input('X='))
y = float(input('Y='))

if (x*x+y*y <= r*r) and ((x <= 0 and y <= 0) or (x >= 0 and y >= (x-1)**2)):
    flag = True
else:
    flag = False

print("Точка X={0: 6.2f} Y={1: 6.2f}".format(x, y), end=" ")
if flag:
    print("попадает", end=" ")
else:
    print("не попадает", end=" ")
print("в область.")
