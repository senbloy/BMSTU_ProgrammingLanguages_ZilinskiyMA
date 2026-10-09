"""Лабораторная 1, вариант 9. Углы задаются в радианах."""
import math


def calculate(alpha, beta):
    if not all(math.isfinite(v) for v in (alpha, beta)):
        raise ValueError("Углы должны быть конечными числами")
    z1 = (math.cos(alpha) - math.cos(beta)) ** 2 - (math.sin(alpha) - math.sin(beta)) ** 2
    z2 = -4 * math.sin((alpha - beta) / 2) ** 2 * math.cos(alpha + beta)
    return z1, z2


def main():
    try:
        alpha, beta = map(float, input("Введите alpha и beta в радианах: ").split())
        z1, z2 = calculate(alpha, beta)
        print(f"z1 = {z1:.12g}\nz2 = {z2:.12g}\nРазность = {abs(z1-z2):.3g}")
    except (ValueError, OverflowError) as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
