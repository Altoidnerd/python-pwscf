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

cqs_yhet = open('Cl12_cq_yhet','r').readlines()
cqs_yhet = [ mistake*float( line.strip() ) for line in cqs_yhet ]

etas_yhet = open('Cl12_eta_yhet','r').readlines()
etas_yhet = [ float( line.strip() ) for line in etas_yhet ]

cqs_ycis = open('Cl12_cq_ycis','r').readlines()
cqs_ycis = [ mistake*float( line.strip() ) for line in cqs_ycis ]

etas_ycis = open('Cl12_eta_ycis','r').readlines()
etas_ycis = [ float( line.strip() ) for line in etas_ycis ]

# angles in deg
angles = range(46)
dangles = angles
# in radians
rangles = [ i*np.pi/180 for i in dangles ]
# square angles
sangles = [ t**2 for t in rangles ]
# cosines
cosangles = [ np.cos(t) for t in rangles ]
cos2angles =[ x**2 for x in cosangles ]
# 3 cos squared theta minus one all over two
cotmoot = [ (3*(np.cos(t))**2 -1 )/2 for t in rangles ]


plt.scatter(sangles, cqs_xcis, color='r', label='in-plane, boat-mode'     , marker='^',s=30 )
plt.scatter(sangles, cqs_xhet, color='b', label='in-plane, chair-mode'    , marker=',',s=30 )
plt.scatter(sangles, cqs_yhet, color='g', label='out-of plane, chair-mode', marker='s',s=30 )
plt.scatter(sangles, cqs_ycis, color='k', label='out-of plane, boat-mode' , marker='o',s=30 )



  #plt.scatter(ecut, etas_pbe_n,  color='g', marker='o', s=65, label='GGA: Cl.pbe-n-kjpaw_psl.1.0.0.UPF')
  #plt.scatter(ecut, etas_pz_nl,  color='r', marker='^', s=65, label='LDA: Cl.pz-nl-kjpaw_psl.1.0.0.UPF')
  #plt.scatter(ecut, etas_pz_n,   color='k', marker='<', s=65, label='LDA: Cl.pz-n-kjpaw_psl.1.0.0.UPF')
  #plt.plot(ecut, etas)

plt.title('Motional effects on Cl coupling constant in C6H4Cl2 molecule')
plt.ylabel("Cl coupling constant")
plt.xlabel("theta_x^2 (in-plane), theta_y^2 (out-of plane), rad^2")

plt.legend(loc=3)
plt.show()  
  


  #plt.ylim(ymin=-547.5)
  #plt.savefig("nqr-freqs-rolling-dt{}-nstep{}-nefgstep{}-nosym-ecut100.pdf".format(dt, nstep, nefgstep))




