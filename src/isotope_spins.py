#!/usr/bin/env python3

f = open('isotope_spins.txt','r').readlines()
meta = [ line for line in f if line.startswith('%') ] 
data = [ line for line in f if line not in meta ] 

def help():
  print(docstring)


def show(query):
  query = str(query)
  relevant = [ line for line in data if (query in line or query.upper() in line or query.lower() in line) ] 
  return relevant


docstring = """
  	 data[N].split()[0] = int: atomic number
                        [1] = int: mass
			[2] = bool: isStable (stable:-, unstable:*)
			[3] = str: symbol
			[4] = str: name
			[5] = float: spin
			[6] = float: g-factor
 			[7] = float: natural-abundance
			[8] = float: quadrupole moment
"""
