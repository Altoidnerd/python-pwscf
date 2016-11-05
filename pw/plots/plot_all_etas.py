#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys

ecut = [#10, 
30,50,70,90,110,130,150,170,190,210]


#/Users/almno10/Desktop/paradichlorobenzene/pbe/1_ecut_conv-n-psl_1.0.0


#  grep '!' scf.* | grep ener
#scf.pbe.ec-10-default-conv-thr.out:!    total energy              =    -540.07258243 Ry
#scf.pbe.ec-110-default-conv-thr.out:!    total energy              =    -547.71705835 Ry
#scf.pbe.ec-130-default-conv-thr.out:!    total energy              =    -547.71727184 Ry
#scf.pbe.ec-150-default-conv-thr.out:!    total energy              =    -547.71738421 Ry
#scf.pbe.ec-170-default-conv-thr.out:!    total energy              =    -547.71744285 Ry
#scf.pbe.ec-190-default-conv-thr.out:!    total energy              =    -547.71747059 Ry
#scf.pbe.ec-210-default-conv-thr.out:!    total energy              =    -547.71749660 Ry
#scf.pbe.ec-30-default-conv-thr.out:!    total energy              =    -547.58384459 Ry
#scf.pbe.ec-50-default-conv-thr.out:!    total energy              =    -547.70956541 Ry
#scf.pbe.ec-70-default-conv-thr.out:!    total energy              =    -547.71537646 Ry
#scf.pbe.ec-90-default-conv-thr.out:!    total energy              =    -547.71664475 Ry


# grep eta efg.* | grep 'Cl  12'

#efg.pbe.ec-10-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -46.0205 MHz  eta= 0.07328
#efg.pbe.ec-110-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.8337 MHz  eta= 0.09451
#efg.pbe.ec-130-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.8364 MHz  eta= 0.09451
#efg.pbe.ec-150-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.8386 MHz  eta= 0.09452
#efg.pbe.ec-170-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.8393 MHz  eta= 0.09451
#efg.pbe.ec-190-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.8385 MHz  eta= 0.09451
#efg.pbe.ec-210-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.8377 MHz  eta= 0.09451
#efg.pbe.ec-30-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.6521 MHz  eta= 0.09424
#efg.pbe.ec-50-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.8336 MHz  eta= 0.09450
#efg.pbe.ec-70-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.8196 MHz  eta= 0.09450
#efg.pbe.ec-90-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.8250 MHz  eta= 0.09451

scf_energy_pbe_n=[
#-540.07258243,
-547.58384459,
-547.70956541,
-547.71537646,
-547.71664475,
-547.71705835,
-547.71727184,
-547.71738421,
-547.71744285,
-547.71747059,
-547.71749660,
]

scf_energy_pbe_nl = [#-547.57580474,
	-547.70945767,
	-547.71779080,
	-547.72020859,
	-547.72087990,
	-547.72118420,
	-547.72131408,
	-547.72137607,
	-547.72142334,
	-547.72145607]


scf_energy_pz_n =[ #-521.41362937,
-529.02763473,
-529.17124281,
-529.17699699,
-529.17805743,
-529.17853084,
-529.17872849,
-529.17882105,
-529.17888537,
-529.17891760,
-529.17893434
]



scf_energy_pz_nl = [#-521.27331016,
-529.01861275,
-529.17043641,
-529.17872831,
-529.18090136,
-529.18161349,
-529.18189900,
-529.18201141,
-529.18207840,
-529.18213020,
-529.18215366
]


Cqs_pbe_n=[#-46.0205,
-68.6521,
-68.8336,
-68.8196,
-68.8250,
-68.8337,
-68.8364,
-68.8386,
-68.8393,
-68.8385,
-68.8377
]

etas_pbe_n = [#0.07328,
0.09424,
0.09450,
0.09450,
0.09451,
0.09451,
0.09451,
0.09452,
0.09451,
0.09451,
0.09451
]





Cqs_pbe_nl=[ #-45.7683,  
-67.9599,  
    -68.2132,  
    -68.1050,  
    -68.0882,  
     -68.0794, 
     -68.0708, 
     -68.0673, 
     -68.0679, 
     -68.0704, 
     -68.0726
] 
 

etas_pbe_nl = [# 0.07343,
0.09514,
   0.09520,
   0.09519,
   0.09519,
   0.09519,
   0.09519,
   0.09519,
   0.09519,
   0.09519,
   0.09519,
]





Cqs_pz_nl = [#-45.9394
-67.8965,
-68.2120,
-68.1028,
-68.0864,
-68.0812,
-68.0739,
-68.0713,
-68.0720,
-68.0744,
-68.0769]

etas_pz_nl = [#0.08007
0.09839,
0.09820,
0.09820,
0.09821,
0.09821,
0.09822,
0.09822,
0.09822,
0.09821,
0.09822
]

Cqs_pz_n = [#-46.1353
-68.7625,
-69.0352,
-69.0258,
-69.0313,
-69.0375,
-69.0376,
-69.0365,
-69.0376,
-69.0382,
-69.0387
]

etas_pz_n = [#0.07995
0.09740,
0.09745,
0.09747,
0.09748,
0.09748,
0.09748,
0.09748,
0.09748,
0.09748,
0.09748
]

#if len(Cqs) != len(etas):
#  print("lengths of vectors to plot are unequal.  Exiting!")
#  sys.exit()

#if len(Cqs) != len(ecut):
#  print("lengths of vectors to plot are unequal.  Exiting!")
#  sys.exit()


plt.scatter(ecut, etas_pbe_nl, color='b', marker='s', s=65, label='GGA: Cl.pbe-nl-kjpaw_psl.1.0.0.UPF')
plt.scatter(ecut, etas_pbe_n,  color='g', marker='o', s=65, label='GGA: Cl.pbe-n-kjpaw_psl.1.0.0.UPF')
plt.scatter(ecut, etas_pz_nl,  color='r', marker='^', s=65, label='LDA: Cl.pz-nl-kjpaw_psl.1.0.0.UPF')
plt.scatter(ecut, etas_pz_n,   color='k', marker='<', s=65, label='LDA: Cl.pz-n-kjpaw_psl.1.0.0.UPF')
#plt.plot(ecut, etas)
plt.title("Asymmetry parameter (eta) for Cl12 in gamma-paradichlorobenzene vs. cutoff energy")
plt.ylabel("eta (dimensionless)")
plt.xlabel("ecutwfc (Ry)")

plt.legend(loc=4)
#plt.ylim(ymin=-547.5)


plt.show()  



