"""
Известно, что рост футболистов в сборной распределен нормально с дисперсией генеральной совокупности, равной 25 кв.см.
Объем выборки равен 27, среднее выборочное составляет 174.2.
Найдите доверительный интервал для математического ожидания с надежностью 0.95.
"""
import numpy as np
import scipy.stats as stats

n = 27
X = 174.2
alfa = 0.05
D = 25
zt = stats.norm.ppf(1 - alfa/2)

d = X - zt * (np.sqrt(D/n))
u = X + zt * (np.sqrt(D/n))

print(f"Доверительный интервал = [{d :.2f};{u :.2f}]")