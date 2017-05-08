#!/usr/bin/env python3

import sys
from dist import Dist
import matplotlib.pyplot as plt

def hist(infile):
  d = Dist(infile)
  angles = []

  for key in d.get_angles().keys():
    for ang in d.get_angles(key).split()[5:]:
      angles.append(float(ang))

  plt.hist(angles)
  plt.title(infile)
  plt.show(block=False)

def main():
  hist(sys.argv[1])

if __name__ == '__main__':
  main()
  
