from math import *
from random import *

n = int(input("Задайте количество элементов в массиве (N<=30) N: "))
if n > 30: n = 30
elif n < 5: n = 5
print("Начальное состояние")
arr = []
for i in range(n):
    arr.append(uniform(-5, 5))
    print("{0: 7.3f}".format(arr[i]), end=" ")
print()

max1 = arr[0]
for i in range(1, len(arr)):
    if abs(max1) < abs(arr[i]):
        max1 = arr[i]
print("Максимальный по модулю элемент списка: {0: 7.3f}".format(max1))

first = -1
second = -1
for i in range(len(arr)):
    if arr[i] > 0:
        if first == -1:
            first = i
        else:
            second = i
            break
if second == -1:
    print("В массиве нет двух положительных элементов")
else:
    asum = 0.0
    for i in range(first + 1, second):
        asum = asum + arr[i]
    print("Сумма элементов между первым и вторым положительными: {0: 7.3f}".format(asum))

print("Список, в котором сохранен порядок ненулевых элементов:")
k = 0
for i in range(len(arr)):
    if arr[i] != 0.0:
        arr[k] = arr[i]
        k += 1
for i in range(k, len(arr)):
    arr[i] = 0.0
for i in range(len(arr)):
    print("{0: 7.3f}".format(arr[i]), end=" ")
print()
