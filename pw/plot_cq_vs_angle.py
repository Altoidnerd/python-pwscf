#!/usr/bin/env python3

import md as md
import datafile as d
import matrix as m
import matplotlib.pyplot as plt
import numpy as nu

nat=24

x=md.Md('md.out')

positions = x.get_trajectory2()

latvecs = m.get_pwi_latvecs('md.in')
positions.pop()

#xyzpositions = []

#for i in positions:
#  xyz = []
#  for j in range(nat):
#    xyz.append(latvecs @ i[j])
#  xyzpositions.append(xyz)


# getting Cl1-C2-C3 bondangles
# must subtract 1 due to zero indexing

Cl_ind= 1 -1
C_ind = 2 -1
C_ind2= 3 -1
angles = []
for k in range(len(positions)):
  # get positions of three atoms in xyz
  p1 = latvecs @ positions[k][Cl_ind] 
  p2 = latvecs @ positions[k][C_ind] 
  p3 = latvecs @ positions[k][C_ind2] 
  # calculate the bond angle
  v1 = p2-p1
  v2 = p3-p2
  dot = v1@v2
  costheta=dot/(m.norm(v1)*m.norm(v2))
  angle =  nu.arccos(costheta)*180/nu.pi-180 
  angles.append(angle)


plt.scatter(angles,list(map(abs,d.Cl1)))
plt.show()


