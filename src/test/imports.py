import md as md
import numpy as np
import matplotlib.pyplot as plt
#import efg as efg
import efg as efg
from efg import *
import magres as mag

pos=md.Md('md.in', 'md.out')
print("md populated as \"pos\"")




efgs=[]
mgs=[]
for i in range(2523):
  fstring='scfs/efg.{}.out'
  fil=efg.Efg(fstring.format(i))
  efgs.append(fil)
  cl=fil.atom(1)
  print(i , is_right_handed(cl.x,cl.y,cl.z))
  #mfstring='scfs/scf-{}.efg.magres'
#  mg=mag.Magres(fstring.format(0))
#  mgs.append(mg)
  
print("efg outs:\tefgs\nmagres files:\tmgs\nmd trajectory:\tpos")

  


