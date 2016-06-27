#!/usr/bin/env python3

import copy

infile = open('all_isotopes_formatted.txt','r').read().split(73*'_')

list_of_lists = []
list_of_dicts = []

infile.pop(0)

for thing in infile:
  list_of_lists.append(
      thing.split('\n')[1:-1] 
  )

mass_dict = { item[0].split()[1]: item for item in list_of_lists }

def lod_factory(k):
  atomic_dict = {}
  for line in list_of_lists[k]:
    atomic_dict[ int( line[8:11] ) ] = sanitize_error(line[12:32] )
  return atomic_dict

def sanitize_error(mass):
  mass = mass.replace(' ','')
  if mass.endswith(')'):
    mass = mass[:-5]
  forbidden = "#()!@$&*"
  for char in forbidden:
    if char in mass:
      mass = mass.replace(char, '')
  return float(mass)

list_of_dicts.append('None')
try:
  for k in range(len(list_of_lists)):
    list_of_dicts.append(lod_factory(k))
except ValueError: 
    pass

lol = copy.deepcopy(list_of_lists)
lod = copy.deepcopy(list_of_dicts)

mass_symboldict = {}
for mass in mass_dict.keys():
  try:
    mass_symboldict[k] = list_of_dicts[ int(mass_dict[k][0][0:2]) ]
  except KeyError:
    pass


