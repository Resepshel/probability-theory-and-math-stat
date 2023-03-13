"""
Произвести вычисления как в пункте 2, но с вычислением intercept.
Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно
(то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации).
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
alfa = 1e-5
b1 = 1
b0 = 300
n = len(x)

for el in range(1000000):
    a = b1 * x + b0
    b0 -= alfa * (2/n) * np.sum(a - y)
    b1 -= alfa * (2/n) * np.sum((a - y) * x)
    if el % 100000 == 0:
        print(f"Iter {el}: b1 = {b1}; b0 = {b0}")

plt.scatter(x, y)
plt.plot(x, b1 * x, label='Без интерсепта')
plt.plot(x, b1 * x + b0, label='С интерсептом')
plt.legend()
plt.show()
