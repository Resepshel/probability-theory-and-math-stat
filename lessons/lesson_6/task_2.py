"""
В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью,
получены опытные данные:
6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей,
оценить истинное значение величины X при помощи доверительного интервала, покрывающего это
значение с доверительной вероятностью 0,95.
"""
import scipy.stats as stats
import numpy as np
from math import sqrt

array = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
n = len(array)
alfa = 0.05
X = np.mean(array)
D = np.var(array, ddof=1)
t = stats.t.ppf(1 - (alfa / 2), 9)

d = X - t * (sqrt(D/n))
u = X + t * (sqrt(D/n))

print(f"Доверительный интервал = [{d :.2f}; {u :.2f}] с 95% покрывает X = {X :.2f}")


