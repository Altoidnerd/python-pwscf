import efg as efg
import md as md
import os

class Efg_collection(object):

  def  __init__(self, target_dir='./scfs/', fstr='efg.{}.out', start=0, limit=10e9, range_like=None, md=None):
    import os
    self.efgs=[]
    self.md = md
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

    
#  def positions(self,step):
 #   if self.md is None:
  #    print("No md data loaded.")
   #   files=os.listdir('.')
    #  if 'md.in' in files and 'md.out' in files:
     #   print('Md data has been located in the current directory {}.\nWould you like to load it?'.format(os.get_cwd()))
      #  prompt='y/n> '
      #  answer=input(prompt)
#        if answer is n:
 #         return 
  #      else:
   #       mddata=md.Md()
    #      self.md=md.Md()
     # return self.md.positions(k)
