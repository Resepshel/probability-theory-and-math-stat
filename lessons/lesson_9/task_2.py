"""
Посчитать коэффициент линейной регрессии при заработной плате (zp), используя градиентный спуск (без intercept).
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
alfa = 1e-6
b1 = 1
n = len(x)

for el in range(2000):
    b1 -= alfa * (2/n) * np.sum((b1 * x - y) * x)
    if el % 400 == 0:
        print(f"Iter {el}: b1 = {b1}")

plt.scatter(x, y)
plt.plot(x, b1 * x)
plt.show()

