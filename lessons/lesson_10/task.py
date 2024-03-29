"""
Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов.
Даны значения роста в трех группах случайно выбранных спортсменов:
Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.
"""
import numpy as np
import scipy.stats as stats
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

f = np.array([173, 175, 180, 178, 177, 185, 183, 182])
h = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
sh = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
# Проверка на нормальность
print(stats.shapiro(f))
print(stats.shapiro(h))
print(stats.shapiro(sh))
# Проверка на равенство дисперсий
print(stats.bartlett(f, h, sh))
# Распределение Фишера
print(stats.f_oneway(f, h, sh))
# Добавляем средние значения в выборки для выравнивания
f2 = np.array([173, 175, 180, 178, 177, 185, 183, 182, 179, 179, 179])
h2 = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180, 178, 178])
sh2 = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170])
# post hoc test Tukey
df = pd.DataFrame({'score': list(np.hstack([f2, h2, sh2])),
                   'group': np.repeat(['Футболисты', 'Хоккеисты', 'Штангисты'], repeats=11)})
tukey = pairwise_tukeyhsd(endog=df['score'],
                          groups=df['group'],
                          alpha=0.05)
print(tukey)
# Статистически значимые различия среди штангистов-футболистов и штангистов-хоккеистов
qq