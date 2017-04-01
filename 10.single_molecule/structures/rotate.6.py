import md as md
import matrix as m
import numpy as np
import sys

#
# theta is angle between Cl-Cl and z-axis
# rotate about y-axis by negative theta
# 
 
x = md.Md('t.pwi')

positions = x.get_trajectory2()[0]




# now we need to rotate about the z-axis
# by pi/2
pos=positions
cls=pos[10:]
clvec = np.array(cls[0]-cls[1])
theta=-m.angle2(-clvec,m.zhat)



t=theta
for i in pos:
  print('C    '+str( m.roty(t) @ i).strip('[]').replace('  ', '     ').replace(' -','    '))


