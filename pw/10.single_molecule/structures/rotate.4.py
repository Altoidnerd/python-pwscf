import md as md
import matrix as m
import numpy as np
import sys

# We attempt to roate the molcule to correct orientation
# by roating the molecule about the z axis
 
x = md.Md('t.pwi')

positions = x.get_trajectory2()[0]




# now we need to rotate about the y-axis
# by the angle the plane makes with the x-axis  
# relevant carbons are 3 and 5

# obtain vector connecting C3, C5
# calcuclate the angle between cvec and the x-axis
pos=positions
cs = np.array([pos[2], pos[4]])
cvec = cs[0] - cs[1]
theta=m.angle2(cvec,m.xhat)

t=theta
for i in pos:
  print('C    '+str( m.roty(t) @ i).strip('[]').replace('  ', '     ').replace(' -','    '))


