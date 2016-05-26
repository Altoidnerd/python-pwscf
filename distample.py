#!/usr/bin/env python3

from dist import Dist

initial_dist = Dist('dist.out')
final_dist = Dist('dist.final.positions.out')
print("initial coordinates:", initial_dist.get_species(), sep='\n')
print("final coordinates:", final_dist.get_species(), sep='\n')

