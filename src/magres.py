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
import numpy as np
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

asobject = dict_to_object



class Magres(object):
  """
  Class for parsing gipaw.x output magres files
  for 'efg' calculation
  """
  
  def __init__(self, magresfile):
    self.magresfile = magresfile
    self.infile = magresfile  
    self.magresfile_array = open(magresfile, 'r').readlines()
    self.file_array = self.magresfile_array
  #  self.labels = self.atom_labels
   # self.specie = set(self.atomic_species)
    #self.data = [None] + [ self.atom(i) for i in range(1,self.nat + 1 ) ] 

  def __repr__(self):
    return "< magres object; magresfile: {}\tlength: {} lines >".format(self.magresfile, len(self.magresfile_array))

  def __str__(self):
    s = ""
    for line in self.file_array:
      s += line
    return s

  def prnt(self):
    for line in self.file_array:
      sys.stdout.write(line)


  #@property
  #def mdstep(self):
  #  def getnum(string):
  #    _ = ""
  #    for i in string:
  #      if i in '0123456789':
   #       _ += i
    #  return int(_)
   # return getnum(self.infile)


  @property
  def nat(self):
    return len(filtr(efg, self.infile))-1

  @property
  def latvecs(self):
    lv1=lmap(float, filtr('lattice', self.file_array)[1].split()[1:])[0:3]
    lv2=lmap(float, filtr('lattice', self.file_array)[1].split()[1:])[3:6]
    lv3=lmap(float, filtr('lattice', self.file_array)[1].split()[1:])[6:9]
    return np.array( [ lv1, lv2, lv3 ] )
    
