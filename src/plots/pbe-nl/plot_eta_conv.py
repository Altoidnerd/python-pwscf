#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys

ecut = [10, 30,50,70,90,110,130,150,170,190,210]


# grep Cq *| grep  'Cl  12'
#
#efg.pbe.ec-10-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -45.7683 MHz  eta= 0.07343
#efg.pbe.ec-110-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.0794 MHz  eta= 0.09519
#efg.pbe.ec-130-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.0708 MHz  eta= 0.09519
#efg.pbe.ec-150-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.0673 MHz  eta= 0.09519
#efg.pbe.ec-170-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.0679 MHz  eta= 0.09519
#efg.pbe.ec-190-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.0704 MHz  eta= 0.09519
#efg.pbe.ec-210-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.0726 MHz  eta= 0.09519
#efg.pbe.ec-30-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -67.9599 MHz  eta= 0.09514
#efg.pbe.ec-50-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.2132 MHz  eta= 0.09520
#efg.pbe.ec-70-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.1050 MHz  eta= 0.09519
#efg.pbe.ec-90-default-conv-thr.out:     Cl  12  Q=        -8.1650 1e-30 m^2  Cq=       -68.0882 MHz  eta= 0.09519

# grep Cq efg.* | grep 'Cl  12' | cut -b84-100
# Cq=       -45.7683 MHz  eta= 0.07343
#  Cq=       -68.0794 MHz  eta= 0.09519
#  Cq=       -68.0708 MHz  eta= 0.09519
#  Cq=       -68.0673 MHz  eta= 0.09519
#  Cq=       -68.0679 MHz  eta= 0.09519
#  Cq=       -68.0704 MHz  eta= 0.09519
#  Cq=       -68.0726 MHz  eta= 0.09519
# Cq=       -67.9599 MHz  eta= 0.09514
# Cq=       -68.2132 MHz  eta= 0.09520
# Cq=       -68.1050 MHz  eta= 0.09519
# Cq=       -68.0882 MHz  eta= 0.09519


Cqs=[-45.7683,  -67.9599,  
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
 

etas = [ 0.07343,
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

if len(Cqs) != len(etas):
  print("lengths of Cq and etas are unequal.  Exiting!")
  sys.exit()

if len(Cqs) != len(ecut):
  print("lengths of (Cq or etas) vectors and ecut are unequal  Exiting!")
  sys.exit()


plt.plot(ecut, etas)
#plt.plot(ecut, etas)
plt.title("Asymmetry parameter for Cl12 in gamma-paradichlorobenzene vs. cutoff energy\npseudo=Cl.pbe-nl-kjpaw_psl-1.0.0.UPF")
plt.ylabel("eta (dimensionless)")
plt.xlabel("ecutwfc (Ry)")
plt.ylim(.07, .1)


plt.show()  
