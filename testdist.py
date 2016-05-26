#!/usr/bin/env python3

from dist import Dist
from unittest import *
import sys

fin = Dist('dist.final.positions.out')

a = Dist('dist.final.positions.out').get_angles()['13']
b = Dist('dist.final.positions.out').get_angles(13)
c = Dist('dist.final.positions.out').get_angles('13')


l = [fin.get_angles(13), fin.get_angles('13'), fin.get_angles()['13'], a, b, c ]
map(sys.stdout.write, l)







