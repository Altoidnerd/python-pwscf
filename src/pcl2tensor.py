#!/usr/bin/env python3
import numpy as np
import sys
a=np.array
#
#
#  Cl18 <-> Cl1
#
#  Cl12 <-> Cl24
#
## eigenvalues, axis 
# from 0th iteration 
# VALID FOR Cl1 <- fix this!!!
Vxx, X =-1.6267, a([ -0.310418, -0.435918,  0.844758 ])
Vyy, Y =-1.9819, a([  0.522549,  0.664099,  0.534711 ])   
Vzz, Z = 3.6086, a([ -0.794093,  0.607411,  0.021640 ])
## eigenvalues, axis 
# from 0th iteration 
# VALID FOR Cl1 <- fix this!!!
cl1Vxx, cl1X =-1.6267, a([ -0.310418, -0.435918,  0.844758 ])
cl1Vyy, cl1Y =-1.9819, a([  0.522549,  0.664099,  0.534711 ])   
cl1Vzz, cl1Z = 3.6086, a([ -0.794093,  0.607411,  0.021640 ])
## eigenvalues, axis 
# from 0th iteration 
# VALID FOR Cl1 <- fix this!!!
cl12Vxx, cl12X =-1.6267, a([  0.310418, -0.435918, -0.844758 ])
cl12Vyy, cl12Y =-1.9819, a([  0.522549, -0.664099,  0.534711 ])   
cl12Vzz, cl12Z = 3.6086, a([ -0.794093, -0.607411,  0.021640 ])

# attempt at a class

class InitialTensor(object):
  def __init__(self):
    self.cl1  = {
	'Vxx':cl1Vxx,
	'Vyy':cl1Vyy,
	'Vzz':cl1Vzz,
	'X':cl1X,
	'Y':cl1Y,
	'Z':cl1Z}
    self.cl18 = self.cl1
    self.cl12 = {
	'Vxx':cl12Vxx,
	'Vyy':cl12Vyy,
	'Vzz':cl12Vzz,
	'X':cl12X,
	'Y':cl12Y,
	'Z':cl12Z}
    self.cl24 = self.cl1

keyword = 'Cl   1'

def get_axes(infile, kw=keyword):
  """
get_axes('efg.*.out') -> array-like
argument is an efg output file

Returns an array containing the
primed principal axes components.
Override the default keyword
using the kw argument.

get_axes(infile)[0] <- X'
get_axes(infile)[1] <- Y'
get_axes(infile)[2] <- Z'
  """
  f = open(infile,'r').readlines()
  relevant = [ line.strip().replace(')','').replace('(','') for line in f if kw in line and 'axis' in line ]
  axes_list = [ line.split()[5:] for line in relevant ] 
  axes_list = a([ list(map(float, axis)) for axis in axes_list ])
  # require the same signs as the refernece set of axes
  if axes_list[0][0] > 0:
    axes_list[0] = -1*axes_list[0]  
  if axes_list[1][0] < 0:
    axes_list[1] = -1*axes_list[1]
  if axes_list[2][0] > 0:
    axes_list[2] = -1*axes_list[2]
  return axes_list

#this_X = get_axes(sys.argv[1])[0]
#this_Y = get_axes(sys.argv[1])[1]
#this_Z = get_axes(sys.argv[1])[2]

#print(this_X,this_Y,this_Z)

#get_axes(sys.argv[1])


def get_angles(infile):
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
  this_X = get_axes(infile)[0]
  this_Y = get_axes(infile)[1]
  this_Z = get_axes(infile)[2]
  theta_X = np.arcsin((this_Z@Y)/np.linalg.norm(Y))
  theta_Y = np.arcsin((this_Z@X)/(np.linalg.norm(X)*np.cos(theta_X)))
  return a( [ theta_X, theta_Y ])


if __name__ == '__main__':
  print(get_axes(sys.argv[1]))
  print(get_angles(sys.argv[1]))
