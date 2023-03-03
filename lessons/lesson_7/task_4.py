"""
Даны 3 группы  учеников плавания.

В 1 группе время на дистанцию 50 м составляют:

56, 60, 62, 55, 71, 67, 59, 58, 64, 67

Вторая группа : 57, 58, 69, 48, 72, 70, 68, 71, 50, 53

Третья группа: 57, 67, 49, 48, 47, 55, 66, 51, 54
"""
import numpy as np
import scipy.stats as stats

# Т.к. выборок больше 2-ух и они независимые, то применяем критерий Крускала-Уоллиса
one = np.array([56, 60, 62, 55, 71, 67, 59, 58, 64, 67])
two = np.array([57, 58, 69, 48, 72, 70, 68, 71, 50, 53])
three = np.array([57, 67, 49, 48, 47, 55, 66, 51, 54])
print(stats.kruskal(one, two, three))

# Т.к. pvalue > альфа = 5%, то делаем вывод в пользу нулевой гипотезы,
# что статистически значимых различий не обнаружено.