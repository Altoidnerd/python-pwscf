#!/usr/bin/env python

import numpy as np

def validate_coords(line):
  nuclei  = 'HHeLiBeBCNOFNeNaMgAlSiPSClArKCaScTiVCrMnFeCoNiCuZnGaGeAsSeBrKrRbSrYZrNbMoTcRuRhPdAgCdInSnSbTeIXeCsBaLaCePrNdPmSmEuGdTbDyHoErTmYbLuHfTaWReOsIrPtAuHgTlPbBiPoAtRnFrRaAcThPaUNpPuAmCmBkCfEsFmMdNoLrRfDbSgBhHsMtDsRgCnUutFlUupLvUusUuo'
  try:
    if line.split()[0] not in nuclei:
      return False
  except IndexError:
    pass
  try:
    xyz = list(map( float, line.split()[1:]))
  except ValueError:
    return False
  try:
    if not list(map(type, xyz )) == [float, float, float]:
      return False
  except ValueError:
      return False

  if not len(line.split()) == 4:
    return False
  else:
    return line

  
def get_coords(infile):
  coords = []
  coords_dict = dict()
  inf = open(infile,'r').read()
  for line in inf.split('\n'):
    if validate_coords(line):
      coords.append(line)
  print("fetched {} positions from {}.".format(len(coords), infile))
  return coords


# make a 3 line string like
#  a11  a12  a13
#  a21  a22  a23
#  a31  a32  a33
# into a numpy matrix

# cleans up unwanted chars at front and end of str

def sanitize_ends(s, targets=' \n\tabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"`}{[]\|/><?~!&^%$#@'):
  while s[0] in targets:
    s = s[1:]
  while s[-1] in targets:
    s = s[:-1]
  return s

def get_matrix(s):
  return np.matrix(sanitize_ends(s).replace('\n',';'))

def get_array(s):
  return np.array([row.split() for row in sanitize_ends(s).split('\n')], float)


def get_cell_params(infile):
  inf = open(infile, 'r').read()
  flines = inf.split('\n')
  params = []
  for line in flines:
    if 'CELL_PARAMETERS' in line:
      ind = flines.index(line)
      params += flines[ind+1:ind+4]
  return np.array([ line.split() for line in params ], float).T


