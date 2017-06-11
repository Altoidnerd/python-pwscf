#!/usr/bin/env python

import sys

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

  
def get_coords_dict(infile):
  coords = []
  for line in infile:
    if validate_coords(line):
      coords.append(line.split())
  return coords

def main():
  if len(sys.argv) > 1:
    inp = open(sys.argv[1], 'r').read()
  else:
    sys.stdout.write('\n...waiting for input from stdin')
    inp = sys.stdin.read()
  #for item in get_coords(inp):
   # sys.stdout.write(item+'\n')

  
  coords = get_coords_dict(inp.split('\n'))
  for site in coords:
    string = "{}\t{}\t{}\t{}\n".format( site[0], site[1], site[2], site[3] )
    sys.stdout.write(string)



if __name__ == '__main__':
  main()





