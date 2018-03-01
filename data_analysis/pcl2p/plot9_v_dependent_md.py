#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


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

exptFit=[
34.35216871,
34.3984564,
34.44460196,
34.49056662,
34.53629613,
34.58171208,
34.62669691,
34.67106584,
34.71451092,
34.75647785,
34.795858,
34.82087468
]

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

calcFit=[
33.76681024,
33.82502047,
33.89191277,
33.96454364,
34.03706338,
34.32436412]

def fitF(a,b,c,T):
  return a+b*T+c/T

def fitExp(T):
  return fitF(35.0232215, -0.002357, -3.1041262, T)

def fitCalc(T):
  return fitF(34.6266672, -0.002923, -1.0001559, T)

dom = np.linspace(50,300,100)
expr_fit       = [ fitExp(item) for item in dom ]
calc_fit       = [ fitCalc(item) for item in dom]

plt.scatter(exptT, exptFq, marker='s', s=35, color='r', label='experiment')
#plt.plot(exptT[:-1], exptFit)
plt.plot(dom, expr_fit, color='r')
plt.scatter(calcT, calcFq, marker='o', s=35,color='g', label='calculated')
#plt.plot(calcT,calcFit)
plt.plot(dom, calc_fit, color='g')

plt.legend(loc=3)

plt.title("")
plt.xlabel("temperature/K")
plt.ylabel('frequency/MHz')
plt.savefig('fig.pdf', format='pdf')

plt.show()
