#!/usr/bin/env python3

import sys

class Dist(object):
  def __init__(self, infile):
    self.file_array = open(infile, 'r').readlines()

  def get_bondlengths(self):
    bonds = []
    limit = len(self.file_array)
    k = 2
    while True:
      bonds.append(self.file_array[k].split()[:-1])
      k += 1
      if len(self.file_array[k].split()) != 5:
        break
      if k >= limit:
        break    
    return bonds

  def get_angles(self, infile):
    angles = []
    

     
