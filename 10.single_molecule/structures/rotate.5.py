import md as md
import matrix as m
import numpy as np
import sys

# We attempt to roate the molcule to correct orientation
# by roating the molecule about the z axis
 
x = md.Md('tt.pwi')

positions = x.get_trajectory2()[0]




# now we need to rotate about the x-axis
# by pi/2
# obtain vector connecting C3, C5
# calcuclate the angle between cvec and the x-axis
pos=positions
theta=np.pi/2

t=theta
for i in pos:
  print('C    '+str( m.rotx(t) @ i).strip('[]').replace('  ', '     ').replace(' -','    '))


