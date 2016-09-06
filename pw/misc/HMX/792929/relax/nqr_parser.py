#!/usr/bin/env python3

import numpy as np
import sys

#################################
#################################
##                           ####
## working version!  tested! ####
##                           ####
#################################
#################################


def f52(cq, eta=0, verbose=False):
    x2 = 1 - 11/54*eta**2
    x1 = 1 + 5/54*eta**2
    return 3 / 10 * cq * np.array( [1/2*x1, x2 ] )

def f32(cq, eta=0):
  return np.sqrt( 1 + (eta**2)/3 ) * cq/2

def f1(cq, eta=0):
  x0 = 2/3 * eta
  x1 = 1 - eta/3
  x2 = 1 + eta/3
  return (3/4) * cq * np.array( [x0, x1, x2] )

def cq32(f, eta=0):
  return np.sqrt( 4 * f**2 / (1 + eta**2 / 3) )



def cq1(freq_arr, eta=0):
  f_0, fmin, fmax = np.sort(np.array([x for x in freq_arr]))
  cq_0    = 2 * f_0/(eta )
  cq_min  = 4 * fmin/( 3 - eta )
  cq_plus = 4 * fmax/( 3 + eta )
  print( """
		
		"cq_0": {},
		"cq_minus": {},
		"cq_plus": {}
		
         """.format(cq_0, cq_min, cq_plus)) 
  return np.array([cq_0, cq_min, cq_plus])

def main():
  
  if len(sys.argv) < 2:
    infile = sys.stdin.read().split('\n') 
  else:
    infile = open(sys.argv[1],'r').readlines()
  relevant_lines = []
  quads = []
  for line in infile:
    try:
      if line.split()[2] == 'Q=':
        relevant_lines.append(line)
    except IndexError: 
      pass

  for line in relevant_lines:
    line = line.replace("eta=-0", "eta= 0")
    quads.append([line.split()[0],line.split()[1],float(line.split()[7]), float(line.split()[10])])
  
  sys.stdout.write('nucleus\tsite\t\tCq(mhz)\teta\t\tv0\t\tv-\t\tv+\n')
  for quad in quads:
    if 'Cl' in quad[0]:
      freq = f32(quad[2],quad[3])
      for thing in quad.append(freq):
        sys.stdout.write(thing+'\t') 

     #print(
       # str(quad[0:2])+':\t\t',f32(quad[2],quad[3])
      #)
    elif 'N' in quad[0]:
      freqs = f1(quad[2], quad[3])
      values_out = [ str(thing) for thing in quad + list(freqs) ] 
      values_out[1] += '\t'
      values_out[3] += '\t'
      for thing in values_out:
      #for thing in [quad[0], quad[1], quad[2], freqs[0], freqs[1], freqs[2]]:
        sys.stdout.write(str(thing) + '\t')
      sys.stdout.write('\n')
    
if __name__ == '__main__':
  main()

