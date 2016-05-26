#!/usr/bin/env python3                   
#
# Copyright (c) 2016 altoidnerd                                                 
#################################################################################
#                                               								#
# Permission is hereby granted, free of charge, to any person obtaining a 	    #
# copy of this software and associated documentation files (the "Software"),	#
# to deal in the Software without restriction, including without limitation 	#
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 	    #
# and/or sell copies of the Software, and to permit persons to whom the 	    #
# Software is furnished to do so, subject to the following conditions:		    #
#										                                        #
# The above copyright notice and this permission notice shall be included 	    #
# in all copies or substantial portions of the Software.			            #
#										                                        #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 	#
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 	    #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 	    #
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 	#
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,	#
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE	#
# THE SOFTWARE.									                                #  
#################################################################################
#
#!/usr/bin/env python3

def float_if_number(var):
  try:
    return float(var)
  except ValueError:
    return str(var)

def format_val(val):
  if type(float_if_number(val)) == float or val == '.true.' or val== '.flase.':
    return "{}".format(val)
  else:
    return "'{}'".format(val)


class Namelist(object):
 
  def __init__(self, name="", content=None):
    uppercase = [
      "",
      "CONTROL",
      "ELECTRONS",
      "SYSTEM",
      "CELL",
      "IONS",
      "INPUTGIPAW",
      "INPUTPH",
      "PATH",
      "INPUTCOND" ]
    valid_namelists = uppercase + [ item.lower() for item in uppercase ]
    self.name = name     
    if content is None:
        self.content = dict()
    else:
        if type(content) != dict:
          raise TypeError("Namelist(name=\"\", content=None)\n\tIf content is not None, content must be of type dict")
        self.content = content
    if self.name not in valid_namelists:
      raise ValueError('{} is not a valid namelist.'.format(self.name))


  def get_val(self, key):
    return self.content[key]
  
  def set_val(self, key, val):
    self.content[key] = float_if_number(val)
  
  def unset(self, key):
    self.content.pop(key)

  def __repr__(self):
    s = ""
    s += '{}{}\n'.format('&', self.name)
    for k in self.content.keys():
      s += "    {}={}\n".format(k, format_val(self.content[k]))
    s += '/\n'
    return s   

def main():
  control = Namelist(name="CONTROL")
  control.set_val("calculation",'scf')
  control.set_val("prefix", "scf.pbe.ecut-80")
  control.set_val("outdir", "./scratch")
  control.set_val("pseudo_dir", "/home/altoidnerd/PSEUDOPOTENTIALS/")
  control.set_val("verbosity","high")
  control.set_val("title","quartz-crystal-scf")
  control.set_val("restart_mode","from_scratch")
  control.set_val("forc_conv_thr",1.0e-4)
  control.set_val("disk_io","low")
  control.set_val("wfcollect",".false.")
  control.set_val("tstress", ".true.")
  for key in ("lorbm", "lberry", "ikpoint_dir"):
    control.set_val(key, ".true.")

  system = Namelist("SYSTEM")
  system.set_val("ibrav", 0)
  system.set_val('a', 9.558)
  system.set_val('c', "8.981")
  system.set_val("ecutwfc", 60)
  system.set_val("ecutrho", 600)
  system.set_val("occupations", 'smearing')
  system.set_val('smearing', 'fermi-dirac')
  system.set_val('degauss', .00367)
  system.set_val('nat', 70)
  system.set_val('ntyp', '6')

  electrons = Namelist("ELECTRONS")
  electrons.set_val("conv_thr", 1e-7)
  electrons.set_val("diago_thr_init", 1e-4)
  electrons.set_val("mixing_beta", '0.7')
  electrons.set_val('diagonalization', 'david')

  print(control, system, electrons)

if __name__ == '__main__':
  main()



