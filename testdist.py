#!/usr/bin/env python3

from __future__ import print_function
from dist import Dist
import sys

fin = Dist('dist.final.positions.out')
a = Dist('dist.final.positions.out').get_angles()['13']
b = Dist('dist.final.positions.out').get_angles(13)
c = Dist('dist.final.positions.out').get_angles('13')

def main():
  print("\nbeginning test ...")
  if sys.version_info[0] == 2:
    map(sys.stdout.write, [fin.get_angles(13), fin.get_angles('13'), fin.get_angles()['13'], a, b, c,'\n' ])
    sys.exit()

  elif sys.version_info[0] == 3:
    print(fin.get_angles(13), fin.get_angles('13'), fin.get_angles()['13'], a, b, c,sep='')
    
if __name__ == '__main__':
  main()






