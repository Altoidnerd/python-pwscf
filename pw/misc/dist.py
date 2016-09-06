#!/usr/bin/env python3

import sys

class Dist(object):

  def __init__(self, infile):
    self.infile = infile
    self.file_array = open(infile, 'r').readlines()
    
    
  def __repr__(self):
    return "<infile:{}  length:{} lines>".format(self.infile, len(self.file_array))

  def __str__(self):
    s = ""
    for line in self.file_array:
      s += line
    return s

  def prnt(self):
    for line in self.file_array:
      sys.stdout.write(line)

  def get_species(self, atomic_symbol=None):
    relevant_lines = []
    species_dict = dict()
    for line in self.get_bond_lines():
      atom_id_1 = line[0]
      atom_id_2 = line[1]    
      species_1 = line[2].split('-')[0]
      species_2 = line[2].split('-')[1]
      species_dict[str(atom_id_1)] = species_1
      species_dict[str(atom_id_2)] = species_2
    
    if atomic_symbol is not None:
      if not type(atomic_symbol) == str:
        raise TypeError("Dist.get_species() takes an optional parameter of type str.")
      return { k: species_dict[k] for k in species_dict.keys() if species_dict[k] == atomic_symbol }
    else:
      return species_dict


  def get_bond_lines(self, atom=None):
    return [ line.split() for line in self.file_array if ( line.endswith(' A  \n') or line.endswith(' A *\n') ) ]


  def get_neighbors(self):
    neighbors = []
    atom_lines = [ line for line in self.file_array if 'neighbors' in line ][1:]
    for line in atom_lines:
      nearest = line.split()[7:11]
      neighbors.append(nearest)
    return neighbors

  def get_angles_list(self):
    angles = []
    angle_lines = [ line for line in self.file_array if 'angles' in line]
    for line in angle_lines:
      angles.append(line.split()[5:11])
    return angles


  def get_angles_lines(self):
    angles = []
    angle_lines = [ line for line in self.file_array if 'angles' in line]
    for line in angle_lines:
      angles.append(line)
    return angles

  def get_neighbor_lines(self):
    return [ line for line in self.file_array if 'species' in line ]


  def get_angles(self, symbol=None):
    angles_dict = dict()
    
    for k in self.get_species().keys():
      angles_dict[k] = self.get_angles_lines()[int(k)-1] 
    # case 1: return the entire dictionary
    if symbol is None:
      return angles_dict
    # case 2: return the angles for species with id = symbol 
    elif type(symbol) is int:
      return angles_dict[str(symbol)]
    # case 3: check if we have case 2 except the index was given as a string
    elif type(symbol) is str:
      try:
        return angles_dict[symbol]
      except KeyError:
    # case 4: return the dictionary subset corresponding to atomic symbol "symbol"
        return { k: angles_dict[k] for k in angles_dict.keys() if k == symbol }
           
