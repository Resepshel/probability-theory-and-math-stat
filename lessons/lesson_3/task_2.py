"""
В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых.
Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. Какова вероятность того, что 3 мяча белые?
"""
from math import factorial

nA = factorial(8) / (factorial(2) * factorial(8 - 2))
nB = factorial(12) / (factorial(4) * factorial(12 - 4))

mA1 = factorial(5) / (factorial(2) * factorial(5 - 2))
mB1 = (factorial(5) / (factorial(1) * factorial(5 - 1))) * (factorial(7) / (factorial(3) * factorial(7 - 3)))

mA2 = (factorial(5) / (factorial(1) * factorial(5 - 1))) * (factorial(3) / (factorial(1) * factorial(3 - 1)))
mB2 = (factorial(5) / (factorial(2) * factorial(5 - 2))) * (factorial(7) / (factorial(2) * factorial(7 - 2)))

mA3 = factorial(3) / (factorial(2) * factorial(3 - 2))
mB3 = (factorial(5) / (factorial(3) * factorial(5 - 3))) * (factorial(7) / (factorial(1) * factorial(7 - 1)))

p1 = (mA1 / nA) * (mB1 / nB)
p2 = (mA2 / nA) * (mB2 / nB)
p3 = (mA3 / nA) * (mB3 / nB)

P = p1 + p2 + p3
print(f"Вероятность того, что 3 мяча белые = {P * 100 :.2f}%")
