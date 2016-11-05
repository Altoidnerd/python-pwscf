#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys

ecut = [#10, 30,
50,70,90,110,130,150,170,190,210]

# ~/paradichlorobenzene/1_ecut_conv-nl-psl_1.0.0  $   grep '!' scf*|grep total
#
#scf.pbe.ec-10-default-conv-thr.out:!    total energy              =    -539.90932664 Ry
#scf.pbe.ec-110-default-conv-thr.out:!    total energy              =    -547.72087990 Ry
#scf.pbe.ec-130-default-conv-thr.out:!    total energy              =    -547.72118420 Ry
#scf.pbe.ec-150-default-conv-thr.out:!    total energy              =    -547.72131408 Ry
#scf.pbe.ec-170-default-conv-thr.out:!    total energy              =    -547.72137607 Ry
#scf.pbe.ec-190-default-conv-thr.out:!    total energy              =    -547.72142334 Ry
#scf.pbe.ec-210-default-conv-thr.out:!    total energy              =    -547.72145607 Ry
#scf.pbe.ec-30-default-conv-thr.out:!    total energy              =    -547.57580474 Ry
#scf.pbe.ec-50-default-conv-thr.out:!    total energy              =    -547.70945767 Ry
#scf.pbe.ec-70-default-conv-thr.out:!    total energy              =    -547.71779080 Ry
#scf.pbe.ec-90-default-conv-thr.out:!    total energy              =    -547.72020859 Ry


scf_energy = [#-547.57580474,
	-547.70945767,
	-547.71779080,
	-547.72020859,
	-547.72087990,
	-547.72118420,
	-547.72131408,
	-547.72137607,
	-547.72142334,
	-547.72145607]

if len(ecut) != len(scf_energy):
  print("lengths of vectors to plot are unequal.  Exiting!")
  sys.exit()

plt.plot(ecut, scf_energy)
plt.title("SCF energy vs cutoff energy (Ry) in gamma-paradichlorobenzene\npseudo=Cl.pbe-nl-kjpaw_psl-1.0.0.UPF")
plt.ylabel("SCF energy (Ry)")
plt.xlabel("ecutwfc (Ry)")
#plt.ylim(ymin=-547.5)


plt.show()  
