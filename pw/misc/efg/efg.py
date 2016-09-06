#!/usr/bin/env python3

import numpy as np

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

