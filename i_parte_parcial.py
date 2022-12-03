# -*- coding: utf-8 -*-
"""I parte parcial

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VZZL0J8oXKIVv9A23-FI1GA_-ZiZOFmr
"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import colors
x1=[0.000000, 0.011400, 0.042800, 0.084700, 0.188500, 0.233400, 0.385400, 0.421000, 0.488200, 0.787200, 0.959200, 1.000000]
x2=[0.000000, 0.318400, 0.530700, 0.822800, 0.983200, 0.990000, 0.998300, 0.999000, 0.999000, 0.999000, 0.999000, 1.000000]
y=[474.03, 463.81, 453.60, 425.76, 389.51, 367.58, 345.35, 338.24, 328.52, 304.69, 299.59, 298.88]

x1=np.arange(0.001)
x2=np.arange(0.001)

y=3*x1**2*np.exp(2*x1)
y=3*x2**2*np.exp(2*x2)

plt.plot=(x1,y)
plt.plot=(x2,y)


plt.xlabel("Fracción Molar del C5H12")
plt.ylabel("temperatura (K)")
plt.title("Fracción Molar del C5H12 en diferentes temperaturas")
plt.grid()
plt.show()

url="https://docs.google.com/spreadsheets/d/1YhMgKH1DyplQshwEvCtvmNgfhamHVsPGqfaY468e0bU/export?format=csv"
df=pd.read_csv(url)
df
fracción=df["y2"]
fracción=df["x1"]
temperatura=df["K"]
plt.plot=(fracción, temperatura)




plt.xlabel("Fracción Molar del C5H12")
plt.ylabel("Temperatura (K)")
plt.title("Fracción Molar del C5H12 en diferentes temperaturas")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

url="https://raw.githubusercontent.com/moisesabregom/parcial2/main/Iparteparcial%20-%20Hoja%201.csv"
df=pd.read_csv(url)
df
fracción=df["y2"]
fracción=df["x1"]
temperatura=df["K"]

plt.plot=(fracción, temperatura)




plt.xlabel("Fracción Molar del C5H12")
plt.ylabel("Temperatura (K)")
plt.title("Fracción Molar del C5H12 en diferentes temperaturas")
plt.show()