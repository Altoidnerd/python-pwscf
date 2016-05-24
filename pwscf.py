#!/usr/bin/env python3

import sys
import copy

class structure(object):
  def __init__(self, filename):
    self.file_array  = open(filename,"r").readlines() 

  def get_file_array(self):
    return self.file_array

  def print_lines(self):
    for k in range(len(self.file_array)):
      print( "line {}:\t{}".format(str(k), self.file_array[k]))

  def get_cell(self):
    tmp = copy.deepcopy(self.file_array)
    for line in tmp:
      if line.startswith("CELL_PARAMETERS"):
        cell_start = tmp.index(line)
    cell = []
    for i in range(4):
      cell.append(tmp[cell_start + i])    
    return cell
