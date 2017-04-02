#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy as np

# dont forget you messed up the Q of Cl

mistake = 8.165/8.065

cqs_xcis = open('Cl12_cq_xcis','r').readlines()
cqs_xcis = [ mistake*float( line.strip() ) for line in cqs_xcis ]

etas_xcis = open('Cl12_eta_xcis','r').readlines()
etas_xcis = [ float( line.strip() ) for line in etas_xcis ]

cqs_xhet = open('Cl12_cq_xhet','r').readlines()
cqs_xhet = [ mistake*float( line.strip() ) for line in cqs_xhet ]

etas_xhet = open('Cl12_eta_xhet','r').readlines()
etas_xhet = [ float( line.strip() ) for line in etas_xhet ]


# angles in deg
angles = range(46)

#plt.scatter(angles, cqs_xcis, color='r', label='in-plane, boat-mode ', marker='^',s=9 )
#plt.scatter(angles, cqs_xhet, color='b', label='in-plane, chair-mode', marker='s',s=9 )

plt.scatter(angles, etas_xcis, color='r', label='in-plane, boat-mode ', marker='^',s=9 )
plt.scatter(angles, etas_xhet, color='b', label='in-plane, chair-mode', marker='s',s=9 )


  #plt.scatter(ecut, etas_pbe_n,  color='g', marker='o', s=65, label='GGA: Cl.pbe-n-kjpaw_psl.1.0.0.UPF')
  #plt.scatter(ecut, etas_pz_nl,  color='r', marker='^', s=65, label='LDA: Cl.pz-nl-kjpaw_psl.1.0.0.UPF')
  #plt.scatter(ecut, etas_pz_n,   color='k', marker='<', s=65, label='LDA: Cl.pz-n-kjpaw_psl.1.0.0.UPF')
  #plt.plot(ecut, etas)

plt.title('Motional effects on Cl asymmetry parameter in C6H4Cl2 molecule')
plt.ylabel("Cl coupling constant")
plt.xlabel("Angle theta_x (deg)")

plt.legend(loc=4)
plt.show()  
  


  #plt.ylim(ymin=-547.5)
  #plt.savefig("nqr-freqs-rolling-dt{}-nstep{}-nefgstep{}-nosym-ecut100.pdf".format(dt, nstep, nefgstep))




