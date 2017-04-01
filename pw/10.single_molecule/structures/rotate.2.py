import md as md
import matrix as m
import numpy as np
import sys

# We attempt to roate the molcule to correct orientation
# by roating the molecule about the z axis
 
x = md.Md('t.pwi')

pos = x.get_trajectory2()[0]


# obtain vector connecting chlorines
cls = pos[10:]
clvec = cls[0] - cls[1]

# calcuclate the angle between clvec and the y axis
yvec = np.array([0,1,0])

dot = clvec @ yvec

costheta = -dot/(m.norm(clvec)*m.norm(yvec))

theta = np.arccos(costheta)

#print(theta,'radians')
#print(theta*180/np.pi,'degrees')

rotmat = []
cos=np.cos
sin=np.sin
theta = -theta
r1 = [ cos(theta), -sin(theta), 0 ]
r2 = [ sin(theta), cos(theta),  0 ]
r3 = [      0    ,     0     ,  1 ]
rows=[r1,r2,r3]

for i in rows:
  rotmat.append(np.array(i))

rotmat = np.array(rotmat)

#print(rotmat)

rotpos = []
for i in pos:
  rotpos.append(rotmat@i)

#for i in rotpos:
#  print('C    '+str(i).strip('[]'))

rotposf = []

for i in rotpos:
  this = []
  for j in i:
    this.append('{:.08f}'.format(j))
  rotposf.append( list( map( float, this)))

for i in rotposf:
  s = str(i)
  print('C   ' + s.strip('[]').replace(',','').replace(' ', '   '))



# now we need to rotate about the y-axis
# by the angle the plane makes with the x-axis  
