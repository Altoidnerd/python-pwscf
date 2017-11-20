#!/usr/bin/env python3

from matrix import *
import numpy as np
import numpy.linalg as la
import time

efgs_dict = dict()
for i in range(1, 25):
  efgs_dict[i] = dict()

spec_data = [[]] + [ la.eigh(get_efg_tensors()[k]) for k in range(1,25) ]

for k in range(1,25):
  tmpdict = dict()
  data = spec_data[k]
 
  mygenvals = data[0]
  lmygenvals = mygenvals.tolist()
  sort_genvals = np.sort( np.abs( spec_data[k][0] )).tolist()
 

  vzzpm = sort_genvals.pop()
  vyypm = sort_genvals.pop()
  vxxpm = sort_genvals.pop()

  print('vzzpm, vyypm, vzzpm', vzzpm, vyypm, vzzpm)
 
  mygenvecs = data[1].T
  lmygenvecs = mygenvecs.tolist()

  print(lmygenvecs)

  if vzzpm in data[0]:
    VZZ = vzzpm
  else: 
    VZZ = -vzzpm

  if vyypm in data[0]:
    VYY = vyypm 
  else:
    VYY = -vyypm

  if vxxpm in data[0]:
    VXX = vxxpm 
  else:
    VXX = -vxxpm


  print("VXX:",VXX)
  print("VYY:", VYY)
  print("VZZ",VZZ)
  
  efgs_dict[k]['Vzz'] = VZZ
  efgs_dict[k]['Vyy'] = VYY
  efgs_dict[k]['Vxx'] = VXX


  efgs_dict[k]['z-axis'] = lmygenvecs[lmygenvals.index(VZZ)]
  efgs_dict[k]['y-axis'] = lmygenvecs[lmygenvals.index(VYY)]
  efgs_dict[k]['x-axis'] = lmygenvecs[lmygenvals.index(VXX)]
 
  


print(efgs_dict) 
