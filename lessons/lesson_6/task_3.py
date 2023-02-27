"""
Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
Рост матерей 178, 165, 165, 173, 168, 155, 160, 164, 178, 175
Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.
"""
import scipy.stats as stats
import numpy as np
from math import sqrt

mothers = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]
daughters = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]
alfa = 0.05
x1 = np.mean(mothers)
x2 = np.mean(daughters)
delta = x1 - x2
D1 = np.var(mothers, ddof=1)
D2 = np.var(daughters, ddof=1)
D = (D1 + D2) / 2
n1 = len(mothers)
n2 = len(daughters)
SE = sqrt(D/n1 + D/n2)
t = stats.t.ppf(1 - (alfa/2), 18)
d = delta - t * SE
u = delta + t * SE

print(f"Доверительный интервал для разности среднего роста = [{d :.2f}; {u :.2f}]")
