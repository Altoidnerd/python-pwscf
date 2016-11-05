#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys

ecut = [#10, 
30,50,70,90,110,130,150,170,190,210]


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
-547.71749660
]

scf_energy_pbe_nl = [#-539.90932664,
        -547.57580474,
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


#plt.scatter(ecut, scf_energy_pbe_nl, color='b', marker='s', s=65, label='GGA: Cl.pbe-nl-kjpaw_psl.1.0.0.UPF' )
#plt.scatter(ecut, scf_energy_pbe_n,  color='g', marker='o', s=65, label='GGA: Cl.pbe-n-kjpaw_psl.1.0.0.UPF'  )
plt.scatter(ecut, scf_energy_pz_nl,  color='r', marker='^', s=65, label='LDA: Cl.pz-nl-kjpaw_psl.1.0.0.UPF'  )
plt.scatter(ecut, scf_energy_pz_n,   color='k', marker='<', s=65, label='LDA: Cl.pz-n-kjpaw_psl.1.0.0.UPF'   )
#plt.plot(ecut, etas)
plt.title("Convergence of ecutwfc in gamma-paradichlorobenzene")
plt.ylabel("SCF energy")
plt.xlabel("ecutwfc (Ry)")

plt.legend(loc=1)
#plt.ylim(ymin=-547.5)


plt.show()  



