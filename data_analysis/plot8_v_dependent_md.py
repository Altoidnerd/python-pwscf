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

nexptFq = [thing/exptFq[-1] for thing in exptFq ]


o100exptT=[
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
]
o100exptFq=[
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
]

no100exptFq = [ thing/o100exptFq[-1] for thing in o100exptFq]
#calcT=[
#291,
#216,
#109,
#49,
#16,
#0]

#calcFq=[
#33.37288,
#34.06817,
#34.2293,
#34.51596,
#34.64037,
#34.6706]

calcT=[
293,
273,
250,
225,
200,
100]

calcFq=[
33.935,
33.889,
33.958,
33.956,
34.0743,
34.4250]

ncalcFq= [ thing/calcFq[-1] for thing in calcFq ]

#plt.scatter(exptT, exptFq, marker='s', s=35, color='r', label='experiment (const. P)')

#plt.scatter(calcT, calcFq, marker='o', s=35,color='g', label='calculated (const. V)')

#plt.scatter(exptT, nexptFq, marker='s', s=35, color='r', label='experiment (const. P)')

#plt.scatter(calcT, ncalcFq, marker='o', s=35,color='g', label='calculated (const. V)')

plt.scatter(o100exptT, no100exptFq, marker='s', s=35, color='r', label='experiment (const. P)')

plt.scatter(calcT, ncalcFq, marker='o', s=35,color='g', label='calculated (including\nvolume correction)')

plt.legend(loc=3)
plt.title('Temperature dependence of \n35Cl NQR frequency of 1,4-dichlorobenzene\ndropped T<100K')
plt.xlabel("temperature/K")
plt.ylabel("nqr frequency fq/MHz")

plt.show()
