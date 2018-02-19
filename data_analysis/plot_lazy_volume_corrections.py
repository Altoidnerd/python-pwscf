#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from nqr_parser6 import f32

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

# the uncorrected ones
calcFq=[
33.37288,
34.06817,
34.2293,
34.51596,
34.64037,
34.6706]
calcFqFrac = [ item/calcFq[-1] for item in calcFq ]
calcFqFrac0 = [ item/calcFq[0] for item in calcFq ]

calcCq_static_293Kcell=69.2296
calcEta_static_293Kcell=0.9844
calcFq_static_293Kcell=f32(calcCq_static_293Kcell,calcEta_static_293Kcell)

# Coefficients by which Cq is reduced,
# and eta is increased via T-dependence
# These coefficients are
# from angular displacements of EFG axes
# use plot_thetas7.py
# on...
# T=293
# T=200 ...
Cq_T_coefficients=[
0.980748,
0.9826,
0.98711,
0.99554,
0.99912,
1.0000]
        
       
Eta_T_coefficients=[
1.066471,
1.033363,
1.050465,
1.023092,
1.002432,
1.00000]

        
# volume corrections are factors
# by which the fq of the lower temperatures 
# should be reduced since all the MD runs
# were done using the crystal cell
# corresponding to the highest temperature.
# these corrections are read from a best fit line
# using the plot of the volume dependence
# of fq with temperature on the horizontal axis
#
# volume_corrections = [ 
# *this one is for calcT[0],
# *this one is for calcT[1],
# ... ]

volume_corrections = [
1.0000,
0.9910,
0.9830,
0.9770,
0.9745,
0.9730]



# now we construct corrected_calcFq
corrected_calcFq= list(np.array(volume_corrections)*np.array(calcFq))
corrected_calcFqFrac = [ item/corrected_calcFq[-1] for item in corrected_calcFq ]
corrected_calcFqFrac0 = [ item/corrected_calcFq[0] for item in corrected_calcFq ]


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


def main():
  plt.scatter(exptT, exptFqFrac, marker='s', s=35, color='r', label='experiment (const. P)')

  plt.scatter(calcT, corrected_calcFqFrac, marker='o', s=35,color='g', label='calculated (const. P)')


  #plt.scatter(volT, volFqFrac, marker='o', s=35,color='g', label='calculated (const. V)')

#  plt.scatter(volT, volFqFrac0, marker='o', s=65,color='g', label='calculated NQR frequency')
#  plt.scatter(volT, volCqFrac0, marker='s', s=25,color='r', label='calculated coupling constant')
  #plt.scatter(volT, volEtaFrac0, marker='>', s=35,color='b', label='calculated asymmetry parameter')

  plt.legend(loc=3)
  plt.title('Volume dependence of \n35Cl NQR frequency of 1,4-dichlorobenzene')
  plt.xlabel("temperature/K at V")
  plt.ylabel("vq/vq(T=0)")

  plt.show()

if __name__ == '__main__':
  main()


