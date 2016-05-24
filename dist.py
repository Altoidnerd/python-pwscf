#!/usr/bin/env python3

import sys

class Dist(object):

  def __init__(self, infile):
    self.file_array = open(infile, 'r').readlines()

  def __repr__(self):
    s = ""
    for line in self.file_array:
      s += line
    return s

  def __str__(self):
    s = ""
    for line in self.file_array:
      s += line
    return s

  def get_bondlengths(self):
    return [line.split() for line in self.file_array if ( line.endswith(' A  \n') or line.endswith(' A *\n') ) ]

  def get_species(self):
    species = dict()
    atom_lines = [line for line in self.file_array if 'neighbors' in line]
    for line in atom_lines:
      pass

  def get_neighbors(self):
    neighbors = []
    atom_lines = [line for line in self.file_array if 'neighbors' in line][1:]
    for line in atom_lines:
      nearest = line.split()[7:11]
      neighbors.append(nearest)
    return neighbors

  def get_angles(self):
    angles = []
    angle_lines = [ line for line in self.file_array if 'angles' in line]
    for line in angle_lines:
      angles.append(line.split()[5:11])
    return angles

def main():
  mydist = Dist('dist.out')
  bonds = mydist.get_bondlengths()
  angles = mydist.get_angles()
#  species = mydist.get_species()
  neighbors = mydist.get_neighbors()
  print(bonds, angles, neighbors)


if __name__ == '__main__':
  main()
