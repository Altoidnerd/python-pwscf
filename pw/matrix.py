#!/usr/bin/env python3

#################################################################################
#										#
# Copyright (c) 2016 Allen Majewski (altoidnerd)				#
# Permission is hereby granted, free of charge, to any person obtaining a 	#
# copy of this software and associated documentation files (the "Software"),	#
# to deal in the Software without restriction, including without limitation	#
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 	#
# and/or sell copies of the Software, and to permit persons to whom the		#	
# Software is furnished to do so, subject to the following conditions:		#
#										#
# The above copyright notice and this permission notice shall be included 	#
# in all copies or substantial portions of the Software.			#
#										#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 	#
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 	#
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 	#
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 	#
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,	#
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE	#
# THE SOFTWARE.									#                                
#										#
#################################################################################

import numpy as np
import os
import sys
import numpy.linalg as la



###################
# scf.in parsiing #
###################

def get_pwi_latvecs(pwi_file=None):
  """
  Opens a pw.x input file and returns a np.matrix
  of the CELL_PARAMETERS card. Recall 
  <alat_coordinates> = latvecs @ <crystal coordinates>
  """
  if pwi_file is None:
    pwi_file = smart_picker('pwi', os.getcwd())
  pwi = open(pwi_file, 'r').readlines()
  
  cell_params_start = min( 
    [ pwi.index(line) for line in pwi 
        if 'CELL_PARAM' in line ]
    )
  params = []
  c = cell_params_start
  return np.array([ line.split() for line in pwi[c+1:c+4] ], float).T

    
def get_pwi_crystal_coords(pwi_file=None, names=False):
  """
  Opens a pw.x input file
  and returns a numpy array of coordinates.
  WARNING: it is zero indexed unline in PWSCF
  and the get_efg_tensors() function
  """
  if pwi_file is None:
    pwi_file = smart_picker('pwi', os.getcwd())  
  pwi = open(pwi_file, 'r').readlines()

  nat = int(sanitize_ends("".join([line for line in pwi if 'nat=' in line])))
  positions_card_startline = min(
    [ pwi.index(line) for line in pwi 
      if 'ATOMIC_POSITIONS' in line]
    )
  p = positions_card_startline
  if not names:
    return np.array([[0,0,0]]+ [ line.split()[1:] for line in pwi[ p: p+nat+1 ]][1:], float)
  return [ line.split() for line in pwi[ p: p+nat+1 ]]



def get_pwi_atomic_species(pwi_file=None, coordinates=False, tostring=False):
  if pwi_file is None:
    pwi_file = smart_picker('pwi', os.getcwd())
  pwi = open(pwi_file,'r').readlines()

  nat = int(sanitize_ends("".join([line for line in pwi if 'nat=' in line])))
  positions_card_startline = min(
    [ pwi.index(line) for line in pwi 
      if 'ATOMIC_POSITIONS' in line]
    )
  p = positions_card_startline
  if not coordinates:
    return [ line.split()[0] for line in pwi[ p: p+nat+1 ]]
  if not tostring:
    return [ line.split() for line in pwi[ p: p+nat+1 ]]
  return [ line for line in pwi[ p: p+nat+1 ]]

def get_pwi_alat_coords(pwi_file=None, tostring=False):
  """
  Retrurns the coordinates in alat units
  """
  latvecs = get_pwi_latvecs(pwi_file)
  if not tostring:
    return np.array([ np.dot(latvecs,vec).tolist() for vec in get_pwi_crystal_coords() ])
  else:
    return [ '  '.join( list( map( str, np.dot(latvecs, vec)))) for vec in get_pwi_crystal_coords() ]


def get_pwi_pseudos(pwi_file=None):
  """
  Returns a list of the pseudopotentials
  used in a pwscf input.
  """
  if pwi_file is None:
    pwi_file = smart_picker('pwi', os.getcwd())
  pwi = open(pwi_file, 'r').readlines()

# pseudo-validation - not yet
#  pseudos_wordlist=[ "UPF","psl","pz","vwm","pbe","blyp","pw91","tpss","coulomb","ae","mt","bhs","vbc","van""rrkj","rrkjus","kjpaw","bpaw"]
  pwi = open(pwi_file, 'r').readlines()
  atomic_species_startline = min( 
    [ pwi.index(line) for line in pwi 
      if 'SPECIES' in line ]
    )
  a = atomic_species_startline
  ntyp = int(sanitize_ends("".join([line for line in pwi if 'ntyp=' in line])))
  species_list = []
  n = a + 1
  while len(species_list) < ntyp:
    if not(set(pwi[n]).issubset({'\n','','\t','\r','!','/'})):
      species_list.append(pwi[n])
      n += 1
    else:
      n += 1

  if len(species_list) == ntyp:
    return [ li.split()[2] for li in species_list ]






###################
# magres parsing  #
###################

def get_efg_tensors(magres_file=None):
  """
  Arguement is a magres format efg outfile.
  Returns a list of EFG matrices (numpy.ndarray), 
  1-indexed as site number in pwscf 
  (the zeroth position is empty).
  """
  if magres_file is None:
    magres_file = [ fil for fil in os.listdir('.') if fil.endswith('magres') ][0]
    print('magres_file <YUP ITS MEH> not specified. Openeing: {}'.format(magres_file))
  magres = open(magres_file,'r').readlines()
  return [ np.array([line.split()[3:6], line.split()[6:9], line.split()[9:12]], float) for line in magres if 'efg' in line ]
    

def get_raw_efg_eigvecs(magres_file=None):
  return np.array( [[]] + [ eigvecs(thing) for thing in get_efg_tensors(magres_file)[1:] ] )

def get_raw_efg_eigvals(magres_file=None):
  return np.array( [[]] + [ eigvals(thing) for thing in get_efg_tensors(magres_file)[1:] ] )

#  
#   We may like to brush the dust off our linear algebra instinct
#
#     efgs = get_efg_tensors()
#     eigenvals = get_raw_efg_eigvals()
#     eigenvecs = get_raw_efg_eigvecs()
# then we have, where is the nuclesr site ndex: 0 <= i <= nat; k is x,y,z so 0 <= k <= 2
#    ( efgs[i] @ eigenvecs[i].T[k] ) / eigenvals[i][k] == eigenvecs[i].T[k]
#
#  though it will not always evaluate to true due to some floating point errors.
#

def get_eigenparis(magres_file=None):
  """
  get_eigenparis()[i][j][k]: 
	i in { 1..nat }; j in {0,1}; k in {0,1,2}
	i: {1..nat} -> atomic specie
	j: {0,1}    -> {eigenvalues, eigenvectos/axes}
	k: {0,1,2}  -> {x,y,z}/{xx,yy,zz}
  """
  return np.array( [[]] + [ (eigvals(thing), eigvecs(thing)) for thing in get_efg_tensors(magres_file)[1:] ] )


def eigenmachine(magres_file=None):
  """
  eigen_machine()[i][k]:
	i in {0, 1}-> {VALS, VECS}
	k in {0, nat -1} -> specie
  NOTE: NOT 1-INDEXED!!! ZERO INDEXED FUNCTION
  """	
  return la.eigh(get_efg_tensors(magres_file)[1:])

    




####################
# efg.out parsing  #
####################

def eigvals(tensor):
  return la.eigh( tensor )[0]

def eigvecs(tensor):
  return la.eigh( tensor )[1]

def get_efgs_dict(magres_file=None):
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

  #  print('vzzpm, vyypm, vzzpm', vzzpm, vyypm, vzzpm)
 
    mygenvecs = data[1].T
    lmygenvecs = mygenvecs.tolist()

   # print(lmygenvecs)

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


    #print("VXX:",VXX)
    #print("VYY:", VYY)
    #print("VZZ",VZZ)
  
    efgs_dict[k]['Vzz'] = VZZ
    efgs_dict[k]['Vyy'] = VYY
    efgs_dict[k]['Vxx'] = VXX


    efgs_dict[k]['z-axis'] = lmygenvecs[lmygenvals.index(VZZ)]
    efgs_dict[k]['y-axis'] = lmygenvecs[lmygenvals.index(VYY)]
    efgs_dict[k]['x-axis'] = lmygenvecs[lmygenvals.index(VXX)]
 
  return efgs_dict  



#####################
# pwscf.out parsing #
#####################


def get_pwo_forces(pwo_file=None):
  if pwo_file is None:
    pwo_file = [ fil for fil in os.listdir('.') if (fil.endswith('out') or fil.endswith('pwo')) and ('scf' in fil or 'relax' in fil or 'md' in fil ) ][0]
    print('No input specified: opening {}'.format(pwo_file))
  
  pwo = open(pwo_file,'r').readlines()
  force_lines = [ line for line in pwo if 'force =' in line ]
  numlines = len(force_lines)
  nat = int(numlines/7)
  return (force_lines[:nat])



####################
# util/helpers     #
####################

def smart_picker(find_type, path='.'):
  if find_type == 'pwi':
    choice = [ fil for fil in os.listdir('.') 
        if ( (fil.endswith('in')  or fil.endswith('pwi')) 
          or 'inp' in fil) 
          and ('scf' in fil 
            or 'relax' in fil 
            or 'md' in fil) ][0]
  if find_type == 'magres':
    choice = [ fil for fil in os.listdir('.') 
      if fil.endswith('magres') ][0]
  if find_type == 'pwo':
    choice = [ fil for fil in os.listdir('.') 
      if (fil.endswith('out') or fil.endswith('pwo')) 
      and ('scf' in fil or 'relax' in fil or 'md' in fil ) ][0]
  print("No input specified. Opening: {}".format(choice))
  return choice

def sanitize_ends(s, targets=' \n\tabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"`}{[]\|/><?~!&^%$#@='):
  while s[0] in targets:
    s = s[1:]
  while s[-1] in targets:
    s = s[:-1]
  return s


