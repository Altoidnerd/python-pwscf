#!/usr/bin/env python3

import numpy as np


# lattice_vectors
lat1 = np.array([14.9113,0,0])
lat2 = np.array([0,6.034,0])
lat3 = np.array([-7.2667500837,0,19.5762965208])

# dot( Tlat, x) = r; x<-crystal, r<-angstrom
Tlat = np.transpose(np.vstack([lat1,lat2,lat3]))


# vector magnitude 

def mag(v):
  summe = 0
  for x in v:
    summe += x**2
  return np.sqrt(summe)


# Thee 3-vectors v1 v2 v3 give the dihedral angle
# where v1 v2 are coplanar and v2 v3 are coplanar
# https://en.wikipedia.org/wiki/Dihedral_angle#cite_note-7

def get_dihedral(v1, v2, v3):
  aux_vec = np.cross(np.cross(v1,v2), np.cross(v2,v3))
  return np.arctan2( np.dot(aux_vec, v2/mag(v2)), aux_vec)
  

# Returns dihedral angle given 4 atomic positions defining two
# planes r1r2r3 and r2r3r4

def get_dihedral4(r1, r2, r3, r4):
  v1 = r2 - r1
  v2 = r3 - r2
  v3 = r4 - r3
  return get_dihedral(v1, v2, v3)


# converts crystal coords r to x y z in angstroms if cp is 
# the matrix of lattice vectors with columns < v1 v2 v3 >

def crystal_to_angstrom(r, cp):
  return np.dot(cp, r)


Cp = np.matrix('14.9113,0,-7.2667500837;0,6.034,0;0,0,19.5762965208')

