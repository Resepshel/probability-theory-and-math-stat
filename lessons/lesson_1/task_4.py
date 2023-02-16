"""
В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
"""

import math as m

favorable_outcomes = 1
all_outcomes = m.factorial(100) / (m.factorial(2) * m.factorial(100 - 2))
result = favorable_outcomes / all_outcomes
print(f'Вероятность того, что 2 приобретенных билета окажутся выигрышными = {result * 100 :.2f}%')
