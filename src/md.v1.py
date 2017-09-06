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


# special paradichlorobenzene stuff
#           [ carbons             ,      hydrogens, chlorines ]
molecule1 = [2,  3,  5, 17, 16, 14,  4,  6, 15, 13,  1, 18]
molecule2 = [23, 8, 10, 11, 20, 22,  7,  9, 19, 21, 24, 12]

class Md(object):
  """
  Ppens a pwo file of an md run,
  parses the file, and can return
  various parameters.
  Use matrix module to load
  lattice vectors.
  """
  # special paradichlorobenzene stuff

  #           [ carbons             ,      hydrogens, chlorines ]
  molecule1 = [2,  3,  5, 17, 16, 14,  4,  6, 15, 13,  1, 18]
  molecule2 = [23, 8, 10, 11, 20, 22,  7,  9, 19, 21, 24, 12]
  
  def __init__(self, infile):
    self.infile = infile
    self.file_array = open(infile, 'r').readlines()
    
    
  def __repr__(self):
    return "<infile:{}  length:{} lines>".format(self.infile, len(self.file_array))

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
      these_positions = [ line.strip().split() for line in self.file_array[ind+1:ind+25] ]
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
      these_positions = [ list( map( float, line.strip().split()[1:])) for line in self.file_array[ind+1:ind+25] ]
      positions.append(np.array(these_positions))
    return positions


