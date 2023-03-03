"""
Исследовалось влияние препарата на уровень давления пациентов. Сначала измерялось давление до приема препарата,
потом через 10 минут и через 30 минут. Есть ли статистически значимые различия?

1е измерение до приема препарата: 150, 160, 165, 145, 155

2е измерение через 10 минут: 140, 155, 150,  130, 135

3е измерение через 30 минут: 130, 130, 120, 130, 125
"""
import numpy as np
import scipy.stats as stats

# Т.к. происходит анализ повторных измерений, то выбираем критерий Фридмана
one = np.array([150, 160, 165, 145, 155])
two = np.array([140, 155, 150, 130, 135])
three = np.array([130, 130, 120, 130, 125])
print(stats.friedmanchisquare(one, two, three))

# Т.к. pvalue < альфа = 1%, то делаем выбор в пользу альтернативной гипотезы,
# что статистически значимые различия обнаружены