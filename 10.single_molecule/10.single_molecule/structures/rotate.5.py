import md as md
import matrix as m
import numpy as np
import sys

 
x = md.Md('t.pwi')

positions = x.get_trajectory2()[0]




# now we need to rotate about the z-axis
# by pi/2
pos=positions
theta=np.pi/2

t=theta
for i in pos:
  print('C    '+str( m.rotz(t) @ i).strip('[]').replace('  ', '     ').replace(' -','    '))


