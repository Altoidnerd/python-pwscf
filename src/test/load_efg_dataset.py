import md as md
import numpy as np
import matplotlib.pyplot as plt
#import efg as efg
import efg as efg
from efg import *
import magres as mag
import efg_collection as ec
from sys import argv

pos=md.Md('md.in', 'md.out')




#efgs=[]
#mgs=[]
#for i in range(2523):
#  fstring='scfs/efg.{}.out'
#  fil=efg.Efg(fstring.format(i))
#  efgs.append(fil)
#  cl=fil.atom(1)
#  print(i , is_right_handed(cl.x,cl.y,cl.z))
  #mfstring='scfs/scf-{}.efg.magres'
#  mg=mag.Magres(fstring.format(0))
#  mgs.append(mg)
  
if len(sys.argv) > 1:
  x=ec.Efg_collection(limit=int(sys.argv[1]))
else:
  
  x=ec.Efg_collection()
print("md populated as \"pos\"")
#print("efg outs:\tefgs\nmagres files:\tmgs\nmd trajectory:\tpos")

  


