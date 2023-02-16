"""
В ящике имеется 15 деталей, из которых 9 окрашены.
Рабочий случайным образом извлекает 3 детали.
Какова вероятность того, что все извлеченные детали окрашены?
"""

import math as m

favorable_outcomes = m.factorial(9) / (m.factorial(3) * m.factorial(9 - 3))
all_outcomes = m.factorial(15) / (m.factorial(3) * m.factorial(15 - 3))
result = favorable_outcomes / all_outcomes
print(f'Вероятность того, что все извлеченные детали окрашены = {result * 100 :.2f}%')
