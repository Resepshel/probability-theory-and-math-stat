"""
Монету подбросили 144 раза.
    Какова вероятность, что орел выпадет ровно 70 раз?
"""

from math import factorial

n = 144
p = 0.5
k = 70
q = 1 - p

Pn = (factorial(n) / (factorial(k) * factorial(n - k))) * (p**k) * (q**(n-k))

print(f'Вероятность того, что орел выпадет ровно 70 раз = {Pn * 100 :.2f}%')
