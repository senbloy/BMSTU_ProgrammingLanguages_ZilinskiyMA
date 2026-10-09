from random import *


def smooth(arr):
    result = []
    for i in range(len(arr)):
        row = []
        for j in range(len(arr[i])):
            total = 0.0
            count = 0
            for k in range(max(0, i-1), min(len(arr), i+2)):
                for t in range(max(0, j-1), min(len(arr[i]), j+2)):
                    if k != i or t != j:
                        total += arr[k][t]
                        count += 1
            row.append(total / count)
        result.append(row)
    return result


def print_matrix(arr):
    for row in arr:
        for value in row:
            print("{0: 8.3f}".format(value), end=" ")
        print()


arr = []
for i in range(10):
    arr.append([])
    for j in range(10):
        arr[i].append(uniform(-5, 5))
print("Начальное состояние")
print_matrix(arr)

result = smooth(arr)
print("Сглаженная матрица")
print_matrix(result)

asum = 0.0
for i in range(10):
    for j in range(i):
        asum += abs(result[i][j])
print("Сумма модулей элементов ниже главной диагонали: {0: 8.3f}".format(asum))
