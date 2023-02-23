"""
Есть ли статистически значимые различия в росте дочерей?
Рост матерей 172, 177, 158, 170, 178,175, 164, 160, 169
Рост взрослых дочерей: 173, 175, 162, 174, 175, 168, 155, 170, 160
"""
import scipy.stats as stats
import numpy as np

mothers = [172, 177, 158, 170, 178, 175, 164, 160, 169]
daughters = [173, 175, 162, 174, 175, 168, 155, 170, 160]

print(stats.ttest_ind(mothers, daughters))

d1 = np.var(mothers, ddof=1)
d2 = np.var(daughters, ddof=1)

m1 = np.mean(mothers)
m2 = np.mean(daughters)

D = 0.5*(d1+d2)

tn = (m1-m2)/np.sqrt(2*D/len(mothers))
print(f"Statistic = {tn}")
print(stats.t.ppf(0.9, 16))
"""
alfa = 10%
Т.к. pvalue > alfa и наблюдаемое значение меньше табличного => 
принимаем нулевую гипотезу, статистически значимых различий нет
"""