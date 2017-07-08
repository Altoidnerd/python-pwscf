import md as md
import matrix as m
import numpy as np
import sys

"""
  Generate x-hetero modes for Cl libration in pcl2phi.
  usage: ./xhet.py arg1
  arg1 is the angle by which
  Cl12 and Cl11 will be rotated
  about the point at the nearest carbon.
"""

if len(sys.argv) > 1:
  theta_y = int(sys.argv[1])*np.pi/180


# We attempt to roate the molcule to correct orientation
# by roating the molecule about the z axis
 
x = md.Md('best.origin.crystal.works.pwi')

pos = x.get_trajectory2()[0]

rc1   = pos[0]
rc11  = pos[10]
rc4   = pos[3]
rcl12 = pos[11]

# these two R's should be identical
# but due to OCD we will define both
# R412: the distance from c4 to cl12
# R111: the distance from c1 to cl11
R412 = m.norm(rc4-rcl12)
R111 = m.norm(rc1-rc11)

sin=np.sin
cos=np.cos

#print("BEFORE!")
#print(pos)

# here rotate Cl12 by reassignment
R=R412
pos[11] = rc4 + np.array([R*sin(theta_y), 0, R*cos(theta_y)])


# here rotate Cl11 by reassignment
R=R111
pos[10] = rc1 + np.array([-R*sin(theta_y), 0, -R*cos(theta_y)])

#print(theta_y)


#print("AFTER")
new_positions=[]
for i in pos:
  new_positions.append(i.tolist())
  
good_prints = []

for i in range(6):
  good_prints.append(['C  ']+new_positions[i])

for i in [6,7,8,9]:
  good_prints.append(['H  ']+new_positions[i])

for i in [10,11]:
  good_prints.append(['Cl ']+new_positions[i])

for i in good_prints:
  sys.stdout.write("{}    {:.12f}    {:.12f}    {:.12f}\n".format(i[0],i[1],i[2],i[3]))
