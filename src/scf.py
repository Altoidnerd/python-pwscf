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



def filtrByComp(term, arr):
  return [ line for line in arr if term in line ]

def filtrByLambda(term, arr):
  return list(filter(lambda x: term in x, arr))

filtr=filtrByComp


class Scf(object):
  """
  Class for parsing pw.x output files
  for 'scf' calculation
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
    self.nat =     int(filtr('nat'    , self.pwifile_array)[0].strip().replace('nat'    ,'').replace('=',''))
    self.ecutwfc = int(filtr('ecutwfc', self.pwifile_array)[0].strip().replace('ecutwfc','').reaplce('=',''))
    self.ecutwfc = int(filtr('ecutrho', self.pwifile_array)[0].strip().replace('ecutrho','').reaplce('=',''))
    self.total_energies = None
    self.temperature = None
     
   

    self.atomic_positions = self.get_atomic_positions()
    

  def __repr__(self):
    return """<pwifile: {}\tlength: {} lines\npwofile: {}\tlength: {} lines>
           """.format(self.pwifile, len(self.pwifile_array), self.pwofile, len(self.pwofile_array))


  def __str__(self):
    s = ""
    for line in self.file_array:
      s += line
    return s

  def prnt(self):
    for line in self.file_array:
      sys.stdout.write(line)

  def get_atomic_positions(self):
    ind = self.pwifile_array.index(filtr('POSITIONS', self.pwifile_array)[0]) 
    positions = self.pwi_file_array[ind+1: ind+self.nat+1]
    return positions
     
