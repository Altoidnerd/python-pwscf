#!/usr/bin/env python3

import sys
import copy




class structure(object):
  def __init__(self, filename):
    self.file_array  = open(filename,"r").readlines() 
    
  def get_file_array(self):
    return self.file_array

  
  def get_cell(self):
    tmp = copy.deepcopy(self.file_array)
    for line in tmp:
      if line.startswith("CELL_PARAMETERS"):
        cell_start = tmp.index(line)
    cell = []
    for i in range(4):
      cell.append(tmp[cell_start + i])    
    return cell

  def get_getpositions(self):
    tmp = copy.deepcopy(self.file_array)
    for line in tmp:
      if line.startswith("ATOMIC_POSITIONS"):
        positions_start = tmp.index(line)
      if line.startswith("K_POINTS"):
        kpoints_start = tmp.index(line) 


  def print_lines(self):
    for k in range(len(self.file_array)):
      print( "line {}:\t{}".format(str(k), self.file_array[k]))


  def get_card(self, card_string):
    tmp_file = copy.deepcopy(self.file_array)
    for line in tmp_file:
      if line.startswith(card_string):
        card_start = tmp.index(line)
    
    
    card = []
    for i in range(4):
      card.append(tmp[cell_start + i])    
    return cell
