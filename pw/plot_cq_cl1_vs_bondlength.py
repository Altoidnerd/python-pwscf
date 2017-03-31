#!/usr/bin/env python3

import md as md
import datafile as d
import matrix as m

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


# getting Cl1-C2 bondlengths
# must subtract 1 due to zero indexing


Cl_ind=1 -1
C_ind=2 -1
distances = []
for k in range(len(positions)):
  # displacement = Cl_xyz_position - Carbon_xyz_position
  displacement = latvecs @ positions[k][Cl_ind] latvecs @ positions[k][C_ind]
  distance = m.norm(displacement)
  distances.append(distance)



