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
exptFqFrac0 = [ item/exptFq[0] for item in exptFq ]

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
calcFqFrac0 = [ item/calcFq[0] for item in calcFq ]


volT = [
293,
273,
250,
225,
200,
100]

vols=[
320.6,
319.2,
316.7 ,
314.8,
311.4,
306.8   
]

volCq=[
68.8365,
68.724,
68.5095,
68.3775,
68.1952,
67.6431
]
volCqFrac = [ item/volCq[-1] for item in volCq ]
volCqFrac0 = [ item/volCq[0] for item in volCq ]

volEta=[
0.09451,
0.09551,
0.09675,
0.0974,
0.09865,
0.10198
]
volEtaFrac = [ item/volEta[-1] for item in volEta ]
volEtaFrac0 = [ item/volEta[0] for item in volEta ]

volFq= [
34.49645,
34.41420,
34.30814,
34.24276,
34.15286,
33.88012
]
volFqFrac = [ item/volFq[-1] for item in volFq ]
volFqFrac0 = [ item/volFq[0] for item in volFq ]

Tcalcdat="""
100	Cl             1             -67.6431        0.10198        -33.88012       -              - 
200	Cl             1             -68.1952        0.09865        -34.15286       -              - 
225	Cl             1             -68.3775        0.0974         -34.24276       -              - 
250	Cl             1             -68.5095        0.09675        -34.30814       -              - 
273	Cl             1             -68.724         0.09551        -34.41420       -              - 
293	Cl             1             -68.8365        0.09451        -34.46945       -              - 
"""
Voldat="""
T                a                 b                 c                 beta                Vol 
300              14.754            5.840             4.025             112.52              320.3
273              14.747            5.830             4.014             112.33              319.2
250              14.730            5.812             3.997             112.24              316.7 
225              14.720            5.801             3.982             112.17              314.8
200              14.705            5.787             3.967             112.00              311.4
100              14.664            5.740             3.925             111.77              306.8   
"""


#plt.scatter(exptT, exptFqFrac, marker='s', s=35, color='r', label='experiment (const. P)')

#plt.scatter(calcT, calcFqFrac, marker='o', s=35,color='g', label='calculated (const. V)')


#plt.scatter(volT, volFqFrac, marker='o', s=35,color='g', label='calculated (const. V)')


volCqFrac0 = [ thing/volCqFrac0[-1] for thing in volCqFrac0 ] 
#plt.scatter(volT, volFqFrac0, marker='s', s=65,color='k', label='calculated NQR frequency')
plt.scatter(volT, volCqFrac0, marker='o', s=55,color='k', label='calculated Cq, normalized')
#plt.scatter(volT, volEtaFrac0, marker='>', s=35,color='b', label='calculated asymmetry parameter')

plt.legend(loc=1, fontsize=15)
plt.title('Volume dependence of calculated\n35Cl NQR frequency 1,4-dichlorobenzene', fontsize=18)
plt.xlabel("temperature/K at V", fontsize=15)
plt.ylabel("Cq(V)/Cq0", fontsize=15)
plt.savefig('pcl2phi_v_dependence_only',format='pdf')
plt.show()


