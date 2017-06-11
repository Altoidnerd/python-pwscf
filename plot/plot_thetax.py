#!/usr/bin/env python3

from get_thetas import *
import os
import matplotlib.pyplot as plt


THETA_X = []
THETA_Y = []

for i in range(2002):
  infile = 'dt60-np8/scfs/efg.{}.out'.format(i)

  try:
    THETA_X.append(get_angles(infile)[0])
  except IndexError:
    pass
  

  try:
    THETA_Y.append(get_angles(infile)[1])
  except IndexError:
    pass


lex = len(THETA_X)
ley = len(THETA_Y)

plt.plot(range(lex), THETA_X)
plt.show()


