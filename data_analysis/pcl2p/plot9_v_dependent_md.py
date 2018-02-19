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


calcT=[
293,
273,
250,
225,
200,
100]

calcFq=[
33.77153,
33.83568,
33.93888,
33.91430,
34.00137,
34.34826]

plt.scatter(exptT, exptFq, marker='s', s=35, color='r', label='experiment')

plt.scatter(calcT, calcFq, marker='o', s=35,color='g', label='calculated')

plt.legend(loc=3)

plt.title("")
plt.xlabel("temperature/K")
plt.ylabel('frequency/MHz')

plt.show()
