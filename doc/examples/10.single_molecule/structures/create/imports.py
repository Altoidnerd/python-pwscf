import md as md
import matrix as m
import numpy as np
import sys

# We attempt to roate the molcule to correct orientation
# by roating the molecule about the z axis
 
x = md.Md('best.origin.ang.pwi')

pos = x.get_trajectory2()[0]


