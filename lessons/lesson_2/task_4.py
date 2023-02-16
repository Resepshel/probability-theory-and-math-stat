"""
В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
Из каждого ящика вытаскивают случайным образом по два мяча.
    Какова вероятность того, что все мячи белые?
    Какова вероятность того, что ровно два мяча белые?
    Какова вероятность того, что хотя бы один мяч белый?
"""

from math import factorial

n1 = factorial(10) / (factorial(2) * factorial(10 - 2))
n2 = factorial(11) / (factorial(2) * factorial(11 - 2))
m1 = factorial(7) / (factorial(2) * factorial(7 - 2))
m2 = factorial(9) / (factorial(2) * factorial(9 - 2))

pAB = (m1 / n1) * (m2 / n2)

print(f'Вероятность того, что все мячи белые = {pAB * 100 :.2f}%')


n1 = factorial(10) / (factorial(2) * factorial(10 - 2))
n2 = factorial(11) / (factorial(2) * factorial(11 - 2))

mA1 = factorial(7) / (factorial(2) * factorial(7 - 2))
mA2 = factorial(2) / (factorial(2) * factorial(2 - 2))

mB1 = factorial(3) / (factorial(2) * factorial(3 - 2))
mB2 = factorial(9) / (factorial(2) * factorial(9 - 2))

mC1 = (factorial(7) / (factorial(1) * factorial(7 - 1))) * (factorial(3) / (factorial(1) * factorial(3 - 1)))
mC2 = (factorial(9) / (factorial(1) * factorial(9 - 1))) * (factorial(2) / (factorial(1) * factorial(2 - 1)))

pA = (mA1 / n1) * (mA2 / n2)
pB = (mB1 / n1) * (mB2 / n2)
pC = (mC1 / n1) * (mC2 / n2)
P = pA + pB + pC

print(f'Вероятность того, что ровно два мяча белые = {P * 100 :.2f}%')


P = 1 - ((3/10) * (2/9) * (2/11) * (1/10))
print(f'Вероятность того, что хотя бы один мяч белый = {P * 100 :.2f}%')
