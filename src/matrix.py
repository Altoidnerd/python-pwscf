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
# basic math tools#
###################

def norm(arr):
  sum = 0 
  for i in arr:
    sum += float(i)**2
  return sum**.5


def angle3(p1,p2,p3):
  """
  Returns the bond angle corresponding
  to three atomic positions.
  You need to pass it numpy arrays
  which is natural if you already
  transformed the coordinates with
  the lattice vectors
  ... returns in degrees
  """
  v1=p2-p1
  v2=p3-p2
  dot = v1@v2
  costheta = dot/(norm(v1)*norm(v2))
  return np.arccos(costheta)*180/np.pi-180

def angle2(r1,r2):
  """
  Returns the angle between
  two vectors.  Pass numpy
  arrays.
  ... returns in RADIANS
  """
  dot = r1@r2
  costheta = dot/(norm(r1)*norm(r2))
  return np.arccos(costheta)

def rotx(theta):
  """
  Returns a rotations matrix
  that rotates a vector by an
  angle theta about the x-axis.
  """
  cos = np.cos
  sin = np.sin
  rotmat = []
  r1 = [      1    ,      0    ,     0     ]
  r2 = [      0    , cos(theta),-sin(theta)]
  r3 = [      0    , sin(theta), cos(theta)]
  rows=[r1,r2,r3]
  
  for row in rows:
    rotmat.append(np.array(row))
  
  return rotmat


def roty(theta):
  """
  Returns a rotations matrix
  that rotates a vector by an
  angle theta about the y-axis.
  """
  cos = np.cos
  sin = np.sin
  rotmat = []
  r1 = [ cos(theta),    0    , sin(theta)]
  r2 = [      0    ,    1    ,     0     ]
  r3 = [-sin(theta),    0    , cos(theta)]
  rows=[r1,r2,r3]
  
  for row in rows:
    rotmat.append(np.array(row))
  
  return rotmat

def rotz(theta):
  """
  Returns a rotations matrix
  that rotates a vector by an
  angle theta about the z-axis.
  """
  cos = np.cos
  sin = np.sin
  rotmat = []
  r1 = [ cos(theta),-sin(theta),    0    ]
  r2 = [ sin(theta), cos(theta),    0    ]
  r3 = [      0    ,      0    ,    1    ]
  rows=[r1,r2,r3]
  for row in rows:
    rotmat.append(np.array(row))
  
  return rotmat

# for testing
# unit vectors
xhat=np.array([1,0,0])
yhat=np.array([0,1,0])
zhat=np.array([0,0,1])
# common angles
t0  =2*np.pi
t30 = np.pi/6
t60 = np.pi/3
t90 =  np.pi/2
t180=  np.pi
t270=3*np.pi/2
t360=t0

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

    
def get_efgs_dict(magres_file=None, nat=24):
  """
  get_efgs_dict('infile')
     -> dict(k,v) where k is an int
      atom index e.g. 1, 2, 3
      and v is a dict of
      efg tensor parameters
   specify option getlist=True
   to return a list instead
  """
  
  efgs_dict = dict()
  for i in range(1, nat+1):
    efgs_dict[i] = dict()

  spec_data = [[]] + [ la.eigh(get_efg_tensors(magres_file)[k]) for k in range(1,nat+1) ]

  for k in range(1,nat+1):
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
  
    efgs_dict[k]['Vzz'] = VZZ
    efgs_dict[k]['Vyy'] = VYY
    efgs_dict[k]['Vxx'] = VXX


    efgs_dict[k]['z-axis'] = lmygenvecs[lmygenvals.index(VZZ)]
    efgs_dict[k]['y-axis'] = lmygenvecs[lmygenvals.index(VYY)]
    efgs_dict[k]['x-axis'] = lmygenvecs[lmygenvals.index(VXX)]
 

  return efgs_dict  


####################
# efg.out parsing  #
####################



def get_axes(infile, kw=None, ref=None):
  """
  get_axes('efg.*.out', kw=None) -> array-like
  argument is an efg output file
  kawrg "kw" specifies which species to display
  kw defaults to 'Cl   1'
  
  e.g. kw -> 'Cl  18'
  Returns an array containing the
  primed principal axes components.
  Override the default keyword
  using the kw argument.
  
  The function returns the axes that are pre-
  computed by QE, though some attempt is made
  to correct algebraic sign instability.
  
  if kawrg 'ref' is specified, the sign conventions
  follow from those of the specie 'ref'
 
  example2:

  > get_axes(infile)[0] <- 'x-axis'
  > get_axes(infile)[1] <- 'y-axis'
  > get_axes(infile)[2] <- 'z-axis'
  
  example2:

  > get_axes(infile, kw='Cl  18', ref='Cl   1')[0] <- 'x-axis'
  > get_axes(infile, kw='Cl  18', ref='Cl   1')[0] <- 'y-axis'
  > get_axes(infile, kw='Cl  18', ref='Cl   1')[0] <- 'z-axis'

  """
  ########    DEFAULTS: Cl   1 ###################################
  #  								 #
  #Vxx, X =-1.6267, np.array([ -0.310418, -0.435918,  0.844758 ])#
  #Vyy, Y =-1.9819, np.array([  0.522549,  0.664099,  0.534711 ])# 
  #Vzz, Z = 3.6086, np.array([ -0.794093,  0.607411,  0.021640 ])#
  #keyword = 'Cl   1'						 #
  ################################################################
  if kw is None:
    kw = 'Cl   1'
    
  f = open(infile,'r').readlines()
  relevant = [ line.strip().replace(')','').replace('(','') for line in f if kw in line and 'axis' in line ]
  axes_list = [ line.split()[5:] for line in relevant ] 
  axes_list = np.array([ list(map(float, axis)) for axis in axes_list ])
  # require the same signs as the refernece set of axes
  if axes_list[0][0] > 0:
    axes_list[0] = -1*axes_list[0]  
  if axes_list[1][0] < 0:
    axes_list[1] = -1*axes_list[1]
  if axes_list[2][0] > 0:
    axes_list[2] = -1*axes_list[2]
  return axes_list







def get_Vijs(infile):
  f = open(infile,'r').readlines()
  relevant = [ line.strip().replace(')','').replace('(','') for line in f if kw in line and 'axis' in line ]
  axes_list = [ line.split()[5:] for line in relevant ] 
  axes_list = np.array([ list(map(float, axis)) for axis in axes_list ])
  
def get_angles(infile, tensor=None):
  """
get_angles('efg.*.out') -> array-like
argument is an efg output file

Returns an array containing the
euler angles for the given
EFG principal axes relative 
to the fixed axes (hard coded).

get_angles(infile)[0] <- theta_X
get_angles(infile)[1] <- theta_Y
  """
  if tensor is None:
    Vxx, X =-1.6267, np.array([ -0.310418, -0.435918,  0.844758 ])
    Vyy, Y =-1.9819, np.array([  0.522549,  0.664099,  0.534711 ])   
    Vzz, Z = 3.6086, np.array([ -0.794093,  0.607411,  0.021640 ])

    
  this_X = get_axes(infile)[0]
  this_Y = get_axes(infile)[1]
  this_Z = get_axes(infile)[2]
  theta_X = np.arcsin((this_Z@Y)/np.linalg.norm(Y))
  theta_Y = np.arcsin((this_Z@X)/(np.linalg.norm(X)*np.cos(theta_X)))
  return np.array( [ theta_X, theta_Y ])



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




#################################
#				#
#	crystal CIF parsing   	#
#				#
#################################

def get_cif_cell_params(cif_infile, *args):
  """
  Returns a dict of keys in *args
  and associated values from the
  specified cif infile
  """
  f = open(cif_infile,'r').readlines()
  d=dict()
  for word in args:
    #print(word)
    good_lines = [ line.strip() for line in f if word in line]
    #print(good_lines)
    data = []
    for line in good_lines:
      data.append(line.split()[-1])
    if len(data) == 1:
      d[word] = data[0]
    else:
      d[word] = data
    for line in good_lines:
      d[line.split()[0]] = line.split()[1]
  return d 


def get_monoclinic_P_latvecs(a,b,c,beta):
  """
  Takes as argument a,b,c, beta
  and produces an array of lattice
  vectors

  get_monoclinic_P_latvecs(a, b, c, beta)
	-> np.array([ v1, v2, v3 ])
  
  ... 
  
  From PW_INPUT.html:
  -12         	Monoclinic P, unique axis b     
		celldm(2)=b/a
 		celldm(3)=c/a,
             	celldm(5)=cos(ac)
      v1 = (a,0,0), v2 = (0,b,0), v3 = (c*cos(beta),0,c*sin(beta))
      where beta is the angle between axis a and c
  

  """
  v1 	=  [a,0,0]
  v2 	=  [0,b,0] 
  v3 	=  [c*np.cos(beta),0,c*np.sin(beta)]
  
  return np.array([v1,v2,v3])


