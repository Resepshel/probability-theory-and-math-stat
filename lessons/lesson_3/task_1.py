"""
Даны значения зарплат из выборки выпускников: 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84,
90, 150. Посчитать (желательно без использования статистических методов наподобие std, var, mean)
среднее арифметическое, среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.
"""
import numpy as np


def average(array):
    summ = 0
    for el in array:
        summ += el
    return summ / len(array)


def svar(array, aver):
    summ = 0
    for el in array:
        summ += (el - aver)**2
    return summ / len(array)


def nvar(array, aver):
    summ = 0
    for el in array:
        summ += (el - aver)**2
    return summ / (len(array) - 1)


array = [100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150]
aver = average(array)
s = svar(array, aver)
n = nvar(array, aver)

print(f"Среднее арифметическое = {aver}")
print(f"Смещенная дисперсия = {s}")
print(f"Несмещенная дисперсия = {n}")
print(f"Среднее квадратичное отклонение смещенной дисперсии = {np.sqrt(s)}")
print(f"Среднее квадратичное отклонение несмещенной дисперсии = {np.sqrt(n)}")
