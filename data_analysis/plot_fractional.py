#!/usr/bin/env python3

import matplotlib.pyplot as plt

exptT=[
280,
260,
240,
220,
200,
180,
160,
140,
120,
100,
80,
20,
0]

exptFq=[
34.327,
34.392,
34.447,
34.502,
34.550,
34.597,
34.640,
34.677,
34.713,
34.745,
34.775,
34.824,
34.829]

exptFqFrac = [ item/exptFq[-1] for item in exptFq ]

calcT=[
291,
216,
109,
49,
16,
0]

calcFq=[
33.37288,
34.06817,
34.2293,
34.51596,
34.64037,
34.6706]

calcFqFrac = [ item/calcFq[-1] for item in calcFq ]

plt.scatter(exptT, exptFqFrac, marker='s', s=35, color='r', label='experiment (const. P)')

plt.scatter(calcT, calcFqFrac, marker='o', s=35,color='g', label='calculated (const. V)')

plt.legend(loc=3)
plt.title('Temperature dependence of \n35Cl NQR frequency of 1,4-dichlorobenzene')
plt.xlabel("temperature/K")
plt.ylabel("vq/v(T=0)")

plt.show()
