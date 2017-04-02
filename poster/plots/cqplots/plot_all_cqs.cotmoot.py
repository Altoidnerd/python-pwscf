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
cotmoot = []
for i in angles:
  cotmoot.append( (3*np.cos(i*np.pi/180)**2 -1)/2)


plt.scatter(cotmoot, cqs_xcis, color='r', label='in-plane, boat-mode ("x-cis")', marker='^',s=9 )
plt.scatter(cotmoot, cqs_xhet, color='b', label='in-plane, chair-mode ("x-het")', marker='s',s=9 )
plt.scatter(cotmoot, cqs_yhet, color='g', label='out-of plane, chair-mode ("y-het")', marker='s',s=9 )
plt.scatter(cotmoot, cqs_ycis, color='k', label='out-of plane, boat-mode ("y-cis")', marker='s',s=9 )


plt.title('Motional effects on Cl coupling constant in C6H4Cl2 molecule')
plt.ylabel("Cl coupling constant")
plt.xlabel("3*(cos(theta)**2 -1)/2")

plt.legend(loc=4)
plt.show()  
  
  #plt.ylim(ymin=-547.5)
  #plt.savefig("nqr-freqs-rolling-dt{}-nstep{}-nefgstep{}-nosym-ecut100.pdf".format(dt, nstep, nefgstep))
