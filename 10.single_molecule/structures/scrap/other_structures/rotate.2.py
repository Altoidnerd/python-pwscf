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

cos=np.cos
sin=np.sin

#print(theta,'radians')
#print(theta*180/np.pi,'degrees')

rotmat = []
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

#for i in rotposf:
#  s = str(i)
# print('C   ' + s.strip('[]').replace(',','').replace(' ', '   '))



# now we need to rotate about the y-axis
# by the angle the plane makes with the x-axis  
# relevant carbons are 3 and 5

# obtain vector connecting C3, C5
cs = np.array([pos[2], pos[4]])
cvec = cs[0] - cs[1]

# calcuclate the angle between clvec and the y axis
xvec = np.array([1,0,0])

dot = cvec @ xvec

costheta = -dot/(m.norm(cvec)*m.norm(xvec))

theta = np.arccos(costheta)

cos=np.cos
sin=np.sin

#print(theta,'radians')
#print(theta*180/np.pi,'degrees')

rotmatx = []
#theta = -theta
r1 = [ cos(theta),    0    , sin(theta)]
r2 = [      0    ,    1    ,     0     ]
r3 = [-sin(theta),    0    , cos(theta)]
rows=[r1,r2,r3]

for i in rows:
  rotmatx.append(np.array(i))

rotmatx = np.array(rotmat)



rotposx = []
for i in rotpos:
  rotposx.append(rotmatx@i)

#for i in rotpos:
#  print('C    '+str(i).strip('[]'))

rotposxf = []

for i in rotposx:
  this = []
  for j in i:
    this.append('{:.08f}'.format(j))
  rotposxf.append( list( map( float, this)))

for i in rotposxf:
  s = str(i)
  print('C   ' + s.strip('[]').replace(',','').replace(' ', '   '))
