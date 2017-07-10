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



class Efg(object):
  """
  Class for parsing gipaw.x output files
  for 'efg' calculation
  """
  
  def __init__(self, efgfile):
    self.efgfile = efgfile
    self.efgfile_array = open(efgfile, 'r').readlines()
    self.file_array = self.efgfile_array
  

  def __repr__(self):
    return "< efg object; efgfile: {}\tlength: {} lines >".format(self.efgfile, len(self.efgfile_array))

  def __str__(self):
    s = ""
    for line in self.file_array:
      s += line
    return s

  def prnt(self):
    for line in self.file_array:
      sys.stdout.write(line)


  @property
  def nat(self):
    return len([ line for line in self.file_array if 'Q=' in line ])

    
  @property
  def WALL_TIME(self):
    return float([ line.split()[4] for line in filtr('WALL',self.file_array) ][-1].replace('s',''))

    
  @property
  def CPU_TIME(self):
    return float([ line.split()[2] for line in filtr('WALL',self.file_array) ][-1].replace('s',''))


  @property
  def atom_labels(self):
    a =  filtr("Q=", self.file_array)
    b =  [ line.strip()[:6] for line in a ]
    return b


  @property
  def atomic_species(self):
    a =  filtr("Q=",self.file_array)
    b =  [ line.split()[0] for line in a ]
    return b


  @property
  def efg_tensors(self, atom=None):
    pass


  @property
  def principle_axes(self):
    axes=[]
    for i in range(self.nat):
      label = self.atom_labels[i]
      vijs = filtr(label, self.file_array)[-4:][:3]
      Xaxis  = lmap(float, filtr('Vxx', vijs)[0].replace(')','').replace('(','').split()[5:])
      Yaxis  = lmap(float, filtr('Vyy', vijs)[0].replace(')','').replace('(','').split()[5:])
      Zaxis  = lmap(float, filtr('Vzz', vijs)[0].replace(')','').replace('(','').split()[5:])
      ax = []
      ax.append(Xaxis)
      ax.append(Yaxis)
      ax.append(Zaxis)
      axes.append(ax)
    return axes



  @property
  def Vii(self):
    viis = []
    for i in range(self.nat):
      label = self.atom_labels[i]
      vijs = filtr(label, self.file_array)[-4:][:3]
      vxx  = float(filtr('Vxx', vijs)[0].split()[3])
      vyy  = float(filtr('Vyy', vijs)[0].split()[3])
      vzz  = float(filtr('Vzz', vijs)[0].split()[3])
      vii  = [vxx,vyy,vzz]
      viis.append(vii)
    return viis
      
      
  @property
  def Qs(self, indices=None):
    a =  filtr("Q=",self.file_array)
    b =  [ line.split()[3] for line in a ]
    return lmap(float, b)
    

  @property
  def Cqs(self, indices=None):
    a =  filtr("Cq=",self.file_array)
    b =  [ line.split()[7] for line in a ]
    return lmap(float, b)


  @property
  def etas(self, indices=None):
    a =  filtr("eta=",self.file_array)
    b =  [ line.split()[10] for line in a ]
    return lmap(float, b)


  def compute_eta(self,atomic_specie_index):
    ind = atomic_specie_index
    return (self.Vii[ind][0] - self.Vii[ind][1])/self.Vii[ind][2]




