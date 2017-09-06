import efg
import os


efgl=[None]*2523

for i in range(2522):
  efgl[i] = efg.Efg('scfs/efg.{}.out'.format(i))


