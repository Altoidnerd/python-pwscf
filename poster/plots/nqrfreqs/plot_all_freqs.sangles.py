#!/usr/bin/env python3


import matplotlib.pyplot as plt
import numpy as np
import nqr_parser6 as nqr

# dont forget you messed up the Q of Cl

mistake = 8.165/8.065

cqs_xcis = open('Cl12_cq_xcis','r').readlines()
cqs_xcis = [ mistake*float( line.strip() ) for line in cqs_xcis ]

etas_xcis = open('Cl12_eta_xcis','r').readlines()
etas_xcis = [ float( line.strip() ) for line in etas_xcis ]

freqs_xcis = [ nqr.f32(cqs_xcis[i],etas_xcis[i]) for i in range(len(cqs_xcis)) ]

cqs_xhet = open('Cl12_cq_xhet','r').readlines()
cqs_xhet = [ mistake*float( line.strip() ) for line in cqs_xhet ]

etas_xhet = open('Cl12_eta_xhet','r').readlines()
etas_xhet = [ float( line.strip() ) for line in etas_xhet ]

freqs_xhet = [ nqr.f32(cqs_xhet[i],etas_xhet[i]) for i in range(len(cqs_xhet)) ]

cqs_ycis = open('Cl12_cq_ycis','r').readlines()
cqs_ycis = [ mistake*float( line.strip() ) for line in cqs_ycis ]

etas_ycis = open('Cl12_eta_ycis','r').readlines()
etas_ycis = [ float( line.strip() ) for line in etas_ycis ]

freqs_ycis = [ nqr.f32(cqs_ycis[i],etas_ycis[i]) for i in range(len(cqs_ycis)) ]

cqs_yhet = open('Cl12_cq_yhet','r').readlines()
cqs_yhet = [ mistake*float( line.strip() ) for line in cqs_yhet ]

etas_yhet = open('Cl12_eta_yhet','r').readlines()
etas_yhet = [ float( line.strip() ) for line in etas_yhet ]

freqs_yhet = [ nqr.f32(cqs_yhet[i],etas_yhet[i]) for i in range(len(cqs_yhet)) ]


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


plt.scatter(sangles, etas_xcis, color='r', label='in-plane, boat-mode (asymmetric)', marker='^',s=20 )
plt.scatter(sangles, etas_xhet, color='b', label='in-plane, chair-mode (symmetric)', marker=',',s=20 )
plt.scatter(sangles, etas_yhet, color='g', label='out-of plane, chair-mode ',        marker='s',s=20 )
plt.scatter(sangles, etas_ycis, color='k', label='out-of plane, boat-mode  ',        marker='o',s=20 )
#plt.scatter(angles, etas_xcis, color='r', label='in-plane, boat-mode ("x-cis")', marker='^',s=15 )
#plt.scatter(angles, etas_xhet, color='b', label='in-plane, chair-mode ("x-het")', marker='s',s=15 )
#plt.scatter(angles, etas_yhet, color='g', label='out-of plane, chair-mode ("y-het")', marker='s',s=15 )
#plt.scatter(angles, etas_ycis, color='k', label='out-of plane, boat-mode ("y-cis")', marker='s',s=15 )

plt.title('Motional effects on Cl asymmetry parameter in C6H4Cl2 molecule')
plt.ylabel("Cl NQR frequency (MHz)")
plt.xlabel("cos(theta_x), cos(theta_y)")

plt.legend(loc=1)
plt.show()  
  


  #plt.ylim(ymin=-547.5)
  #plt.savefig("nqr-freqs-rolling-dt{}-nstep{}-nefgstep{}-nosym-ecut100.pdf".format(dt, nstep, nefgstep))




