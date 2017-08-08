import md as md
import numpy as np
import matplotlib.pyplot as plt
import efg as efg
import efgdev as efgdev
from efg import *

#xmd=md.Md('md.in', 'md.out')

#pos1=x.get_trajectory1()
#pos2=x.get_trajectory2()
#pos3=x.get_trajectory3()


#fstring='scfs/efg.{}.out'
#xefg=efg.Efg(fstring.format(0))
#xefgdev=efg.Efg(fstring.format(0))


import magres as mg
fstring='scfs/scf-{}.efg.magres'
xmg=mg.Magres(fstring.format(0))


