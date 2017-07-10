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

#   python-pwscf was designed for python3; 
#   run on > 2.7 at your own risk.						

import sys
import matplotlib.pyplot as plt
import numpy as np
import matrix



#########################################
#   See efg.py for documentation of	#
#   the following functions.		#
#########################################
def filtr(pattern, array):
  return list( filter( lambda x: pattern in x, array ) )

def indices(pattern, array):
  return [ array.index(thing) for thing in filtr(pattern, array) ]

def lmap(func, array):
  return list( map( func, array ) ) 



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
  
  def __init__(self, pwifile, pwofile):
    self.pwifile = pwifile
    self.pwifile_array = open(pwifile, 'r').readlines()
    self.pwofile = pwofile
    self.pwofile_array = open(pwofile, 'r').readlines()
    self.file_array = self.pwifile_array + self.pwofile_array
    # ascertain nat
    nat = [ line for line in self.file_array if 'nat' in line ][0]
    self.nat = int(nat.strip().replace('nat=',''))
    
    
    self.latvex = self.lv

    self.trajectory = self.get_trajectory3()
    self.crys_pos= self.trajectory

    self.xyzpos = [ self.latvex @ thing for thing in self.crys_pos ]
   

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
    self.file_array
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
    self.file_array
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
    self.file_array
    inds = [ i for i,x in enumerate(self.file_array) if "ATOMIC_POSITIONS" in x ] 
    for ind in inds:
      these_positions = [ list( map( float, line.strip().split()[1:])) for line in self.file_array[ind+1:ind+self.nat+1] ]
      positions.append(these_positions)
    return positions




  def get_pwi_latvecs(self, pwi_file=None):
    """
    Opens a pw.x input file and returns a np.matrix
    of the CELL_PARAMETERS card. Recall 
    <alat_coordinates> = latvecs @ <crystal coordinates>
    """
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
    self.latvecs = np.array([ line.split() for line in pwi[c+1:c+4] ], float).T
    self.inv_latvecs = np.linalg.inv(self.latvecs)
    return self.latvecs


  @property
  def lv(self):
    return self.get_pwi_latvecs(pwi_file=None)
  


  def pprint_coors(self,positions):
    pos = positions
    for i in pos:
      print('C    '+str(i).strip('[]').replace('  ','    ').replace(' -','   '))    



def get_string(positions):
  pos = positions
  for i in pos:
    return 'C    '+str(i).strip('[]').replace('  ','    ').replace(' -','   ')














