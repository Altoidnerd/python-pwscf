#!/usr/bin/env python3

import numpy as np


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


