#!/usr/bin/env python3
#
#
#
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

#   python-pwscf was designed for python3; 
#   run on > 2.7 at your own risk.						

import sys
import matplotlib.pyplot as plt
import numpy as np
import matrix as mat
from nqr_parser import f32

def filtr(pattern, array):
  """
  filtr(str "parrtern", list array): -> list
  
    returns a new list containing the elements
    in array for which "pattern" is matched.
  """
  return list( filter( lambda x: pattern in x, array ) )

def indices(pattern, array):
  """
  indices(str "pattern", array): -> list
  
    returns a new list containing the indices 
    of the elements in array that match "pattern."
  """
  return [ array.index(thing) for thing in filtr(pattern, array) ]

def lmap(func, array):
  """
  lmap(function, array): -> list

  just like python map, but returns a list instead of a
 """
  return list( map( func, array ) ) 

def dict_to_object(dict_item):
  d = dict_item
  class _:
    pass
  for key, value in d.items():
    setattr(_, key, value)
  return _




class Md(object):
  """
  Opens a pwo file of an md run,
  parses the file, and can return
  various parameters.
  Use matrix module to load
  lattice vectors.
  """
  # special paradichlorobenzene stuff

  #           [ carbons             ,      hydrogens, chlorines ]
  molecule1 = [2,  3,  5, 17, 16, 14,  4,  6, 15, 13,  1, 18]
  molecule2 = [23, 8, 10, 11, 20, 22,  7,  9, 19, 21, 24, 12]
  
  def __init__(self, pwifile='md.in', pwofile='md.out'):
    self.pwifile = pwifile
    self.pwofile = pwofile
#    print("opening infile: {}\nopening outfile: {}".format(pwifile,pwofile))
    self.pwifile_array = [ line.strip() for line in open(pwifile, 'r').readlines()]
    self.pwofile_array = [ line.strip() for line in open(pwofile, 'r').readlines()]
    self.file_array = self.pwifile_array + self.pwofile_array
    # ascertain nat
    nat = filtr('nat', self.file_array)[0]
    self.nat = int(nat.strip().replace('nat=',''))


  def __repr__(self):
    return "<pwifile: {}\tlength: {} lines\npwofile: {}\tlength: {} lines>".format(self.pwifile, len(self.pwifile_array), self.pwofile, len(self.pwofile_array))

  def __str__(self):
    s = ""
    for line in self.file_array:
      s += line
    return s

  def prnt(self):
    for line in self.file_array:
      sys.stdout.write(line)

    
  def get_trajectory1(self):
    """
    returns trajectory as a list of lists
    each of which contains the name of the 
    species and string representations
    of their positions in the units specified
    in md output.
    """
    positions = []
    inds = [ i for i,x in enumerate(self.file_array) if "ATOMIC_POSITIONS" in x ] 
    for ind in inds:
      these_positions = [ line.strip() for line in self.file_array[ind+1:ind+self.nat+1] ]
      positions.append(these_positions)
    return positions
  
  def get_trajectory2(self):
    """
    returns trajectory as a list of numpy 
    arrays each of which contains on the the 
    float representations positions of the
    atomic species
    """
    positions = []
    inds = [ i for i,x in enumerate(self.file_array) if "ATOMIC_POSITIONS" in x ] 
    for ind in inds:
      these_positions = [ list( map( float, line.strip().split()[1:])) for line in self.file_array[ind+1:ind+self.nat+1] ]
      positions.append(np.array(these_positions))
    return positions

  def get_trajectory3(self):
    """
    returns trajectory as a list of lists 
    each of which contains on the the 
    float representations positions of the
    atomic species
    """
    positions = []
    inds = [ i for i,x in enumerate(self.file_array) if "ATOMIC_POSITIONS" in x ] 
    for ind in inds:
      these_positions = [ list( map( float, line.strip().split()[1:])) for line in self.file_array[ind+1:ind+self.nat+1] ]
      positions.append(these_positions)
    return positions

  @property
  def atom_labels(self):
    labels=[]
    ind = indices('POS', self.pwifile_array)[0] 
    first_positions = self.pwifile_array[ind: ind+self.nat+1]
    return [None]+[ line.split()[0].strip() for line in first_positions ][1:]

  

  def get_latvex(self, pwi_file=None, return_as='array'):
    """
    get_latvex(pwi_file=None, return_as='array')

    ->If optional param return_as='array':
    Opens a pw.x input file and returns a np.matrix
    of the CELL_PARAMETERS card. Recall 
    <alat_coordinates> = latvecs @ <crystal coordinates>
    
    ->If optional param return_as='string'
    
    """
    if pwi_file is None:
      pwi = self.pwifile_array
    else:
      pwi = open(pwi_file, 'r').readlines()
    if return_as == 'array':
  
      cell_params_start = min( 
        [ pwi.index(line) for line in pwi 
            if 'CELL_PARAM' in line ]
        )
      params = []
      c = cell_params_start
      return np.array([ line.split() for line in pwi[c+1:c+4] ], float).T
    
    if return_as == 'string':
      return self.get_lvs_as_str()


  @property
  def latvex_array(self, pwi_file=None):
    if pwi_file is None:
      pwi = self.pwifile_array
    else:
      pwi = open(pwi_file, 'r').readlines()
  
    cell_params_start = min( 
      [ pwi.index(line) for line in pwi 
          if 'CELL_PARAM' in line ]
      )
    params = []
    c = cell_params_start
    return np.array([ line.split() for line in pwi[c+1:c+4] ], float).T

  @property
  def latvex_string(self):
    vex = self.get_latvex(return_as='string')  
    s = ''
    for vec in vex:
      s += vec+'\n'
    return s


  def get_cell_volume(self):
    a = self.latvex_array.T[0]
    b = self.latvex_array.T[1]
    c = self.latvex_array.T[2]
    cell_volume = a @ np.cross(b,c)
    return cell_volume
  
  @property
  def cell_volume(self):
    return self.get_cell_volume()

  def get_lvs_as_str(self):
    """
    """
    lvs = []
    inds = [ i for i,x in enumerate(self.file_array) if "CELL_PARAMETERS" in x ] 
    for ind in inds:
      num_latvex = 3
      # much like get_trajectory1() except 3=1 instead of self.nat+1
      these_lvs = [ line.strip() for line in self.file_array[ind+1:ind+num_latvex+1] ]
      lvs.append(these_lvs)
    return these_lvs

  
  def positions(self, step):
    return self.all_positions[step]


  @property
  def all_positions(self):
    return self.get_trajectory3()

  @property
  def atomic_species(self):
    return set(self.atom_labels[1:])

  @property
  def ntyp(self):
    return len(self.atomic_species)

   

  def pprint_coors(self,positions):
    pos = positions
    for i in pos:
      print('C    '+str(i).strip('[]').replace('  ','    ').replace(' -','   '))    



def get_string(positions):
  pos = positions
  for i in pos:
    return 'C    '+str(i).strip('[]').replace('  ','    ').replace(' -','   ')














