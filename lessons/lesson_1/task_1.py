"""
Из колоды в 52 карты извлекаются случайным образом 4 карты.
    a) Найти вероятность того, что все карты – крести.
    б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
"""

import math as m

all_carts = 52
carts_take = 4
cross = 13

favorable_outcomes_1 = m.factorial(cross) / (m.factorial(carts_take) * m.factorial(cross - carts_take))
all_outcomes_1 = m.factorial(all_carts) / (m.factorial(carts_take) * m.factorial(all_carts - carts_take))
result_1 = favorable_outcomes_1 / all_outcomes_1
print(f'Вероятность того, что все карты - крести = {result_1 * 100 :.2f}%')


P1 = (m.factorial(4) / (m.factorial(1)*m.factorial(4 - 1))) * (m.factorial(48) / (m.factorial(3)*m.factorial(48 - 3)))
P2 = (m.factorial(4) / (m.factorial(2)*m.factorial(4 - 2))) * (m.factorial(48) / (m.factorial(2)*m.factorial(48 - 2)))
P3 = (m.factorial(4) / (m.factorial(3)*m.factorial(4 - 3))) * (m.factorial(48) / (m.factorial(1)*m.factorial(48 - 1)))
P4 = m.factorial(4) / (m.factorial(4)*m.factorial(4 - 4))
favorable_outcomes_2 = P1 + P2 + P3 + P4
all_outcomes_2 = m.factorial(52) / (24 * m.factorial(48))
result_2 = favorable_outcomes_2 / all_outcomes_2
print(f'Вероятность того, что среди 4-х карт окажется хотя бы один туз = {result_2 * 100 :.2f}%')