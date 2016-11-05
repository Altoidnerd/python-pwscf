#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys

# pw.x options
################
# ion initial kick temp = 300K
# dt = 50 a.u. (Ry) = 50*4.8378e-17 s 
# N_step = 300
#
#
#
# basic data
#################
# Ekins = [ ... ]
# Etots = [ ... ]
# temperatures = [ ... ]
#
#
#
# derived lists
#################
# Epots = [ Etots[i] - Ekins[i] for i in range(len(Ekins)) ] 
# norm_Etots = [ thing/Etots[0] for thing in Etots ]
# diff_Etots = [ thing - Etots[0] for thing in Etots ]
# average_temp = get_mean(temperatures)
# inds = range(len(Ekins))

dt=50
ry_atomic_time=4.8378e-17 #seconds per a.u.
timestep_SI = dt*ry_atomic_time
tempw=600

def get_mean(li):
  summe = 0
  for item in li:
    summe += item
  return int(summe/len(li))

def main():
  #plt.scatter(inds, Ekins, color='b', marker='s', s=65, label='Kinetic Energy (Ry)')
  plt.plot(inds, Ekins, color='g', label='E_kinetic (Ry)')
  #plt.plot(inds, norm_Etots, color='r', label='E_total[t]/(-548.00599230 Ry)')
  #plt.plot(inds, diff_Etots, color='k', label='E_total[t] - E_total[0] = E_total[t] + 548.00599230 Ry')
  #plt.plot(inds, temperatures, color='k', label='cell temperature (K)')
  plt.plot(inds, normtemps, color='k', label='scaled cell temperature (K)\ntemperature[i]/{}K'.format(temperatures[0]))


  #plt.scatter(ecut, etas_pbe_n,  color='g', marker='o', s=65, label='GGA: Cl.pbe-n-kjpaw_psl.1.0.0.UPF')
  #plt.scatter(ecut, etas_pz_nl,  color='r', marker='^', s=65, label='LDA: Cl.pz-nl-kjpaw_psl.1.0.0.UPF')
  #plt.scatter(ecut, etas_pz_n,   color='k', marker='<', s=65, label='LDA: Cl.pz-n-kjpaw_psl.1.0.0.UPF')
  #plt.plot(ecut, etas)

  plt.title("p-Cl_2-benzene MD, tempw={}K, dt={} a.u., T_avg={}K".format(tempw, dt, get_mean(temperatures)))
  plt.ylabel("Ry")
  plt.xlabel("time (simulation step: {} a.u. per step\n1 a.u. = {}s\n{}a.u. = {}s".format(dt, ry_atomic_time, dt, timestep_SI))


  print(average_temp)
  plt.legend(loc=1)

  #plt.ylim(ymin=-547.5)

  plt.show()  



#### put big data vectors here

Etots = [-547.94043922,
-547.91814888,
-547.92579061,
-547.91473659,
-547.93357748,
-547.90736205,
-547.91181243,
-547.89919761,
-547.92336420,
-547.87102976,
-547.85803741,
-547.84274262,
-547.87038196,
-547.72896839,
-547.53627680,
-547.52737810,
-547.53597326,
-547.52648266,
-547.65625838,
-540.91790668,

]

Ekins = [0.13110616,
0.10399564,
0.09044183,
0.05781528,
0.07719291,
0.07146298,
0.09371037,
0.07189203,
0.10143926,
0.08043332,
0.11551919,
0.06130702,
0.12294451,
0.06914570,
0.28331929,
0.08723635,
0.08958399,
0.23337281,
0.36526952,
5.31706797
]

temperatures = [600.00000000,
475.93026279,
413.90196558,
264.58838247,
353.26902379,
327.04634803,
428.86027536,
329.00986628,
464.23113272,
368.09859784,
528.66712558,
280.56814444,
562.64869216,
316.44143318,
1296.59489456,
399.23228247,
409.97611951,
1068.01763067,
1671.63557384,
24333.26474286
]



Epots = [ Etots[i] - Ekins[i] for i in range(len(Ekins)) ] 
norm_Etots = [ thing/Etots[0] for thing in Etots ]
diff_Etots = [ thing - Etots[0] for thing in Etots ]
average_temp = get_mean(temperatures)
normtemps = [ thing / temperatures[0] for thing in temperatures ]

inds = range(len(Ekins))

if __name__ == '__main__':
  main()



