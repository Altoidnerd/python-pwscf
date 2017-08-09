import efg as efg
import md as md
import os

class Efg_collection(object):

  def  __init__(self, target_dir='./scfs/', fstr='efg.{}.out', start=0, limit=10e9, range_like=None, md_init=None):
    import os
    self.efgs=[]
    self.md_init = md_init
    if range_like is None:
      print('loading all efg data from: {}'.format(target_dir))
      print('format string is: {}'.format(fstr.format('index')))
      i=start
      while i < limit:
        try:
          target = os.path.normpath(target_dir+fstr.format(i))
          e=efg.Efg(target)
          self.efgs.append(e)
          print('added {}'.format(fstr.format(i)))
          i+=1
        except FileNotFoundError:
          print("Done: {} efg outputs populated".format(len(self.efgs)))      
          break     

  @property
  def step(self, k):
   return self.efgs[k]

  @property
  def size(self):
    return len(self.efgs)

  @property
  def mddata(self,inf='md.in',outf='md.out'):
    if self.md_init is None:
      try:
        return md.Md(inf,outf)
      except FileNotFoundError:
        print("No MD data found in {}".format(os.get_cwd()))
        return self.md_init

  @property
  def positions(self,step):
    try:
      return self.mddata.positions(step)
    except AttributeError:
      return self.md_init


