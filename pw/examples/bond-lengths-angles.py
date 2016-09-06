#!/usr/bin/env python3

from dist import Dist
import sys

sys.path.append("$USER/python-pwscf/pw/")


fin = Dist('misc/dist.final.positions.out')
a = Dist('misc/dist.final.positions.out').get_angles()['13']
b = Dist('misc/dist.final.positions.out').get_angles(13)
c = Dist('misc/dist.final.positions.out').get_angles('13')

def main():
  print("\nbeginning test ...")
  if sys.version_info[0] == 2:
    map(sys.stdout.write, [fin.get_angles(13), fin.get_angles('13'), fin.get_angles()['13'], a, b, c,'\n' ])
    sys.exit()

  elif sys.version_info[0] == 3:
    print(fin.get_angles(13), fin.get_angles('13'), fin.get_angles()['13'], a, b, c,sep='')
    
if __name__ == '__main__':
  main()






