#!/usr/bin/env python3

import numpy as np
import numpy.linalg as la
from matrix import *
from constants import atomic_nums

f = open('scf.out.xsf','r').readlines()

for i in range(18,42):
  a = f[i]
  f[i] = a.split()[:-3]

# making the secton isomorphic to the
# get sequences which are 1-indexed

section_copy = f[17:42]
sc = section_copy
sc[0] = ''

# do this 3x

for k in [0,6,12,23]:
  for i in "111":
    f.insert( 42 - k , sc[24 - k])

# this duplicated the coordinates 
# (added 3x dummies at each chlorine = 17)

# now need nat=36 not 24

f[17] = f[17].replace('24','36')

print('sections of f here...5-80')
for line in f[:100]:
  print(line)

ed = get_efgs_dict()

Cl1Vzz, Cl1Vyy, Cl1Vxx = ed[1]['Vzz'], ed[1]['Vyy'], ed[1]['Vxx']
# unit vectors

Cl1zUvec = np.array(ed[1]['z-axis'])
Cl1yUvec = np.array(ed[1]['y-axis'])
Cl1xUvec = np.array(ed[1]['x-axis'])

Cl1xvec = np.array(ed[1]['x-axis'])*Cl1Vxx
Cl1yvec = np.array(ed[1]['y-axis'])*Cl1Vyy
Cl1zvec = np.array(ed[1]['z-axis'])*Cl1Vzz

print('Cl1: Vxx, Vyy, Vxx ...')
print(Cl1Vxx, Cl1Vyy, Cl1Vzz)
print(Cl1xUvec)
print(Cl1yUvec)
print(Cl1zUvec)

f[19] = f[19] + (np.array( ed[1]['x-axis'])*ed[1]['Vxx']).tolist()
f[20] = f[20] + (np.array( ed[1]['y-axis'])*ed[1]['Vyy']).tolist()
f[21] = f[21] + (np.array( ed[1]['z-axis'])*ed[1]['Vzz']).tolist()


for line in f[:70]:
  print(line)

