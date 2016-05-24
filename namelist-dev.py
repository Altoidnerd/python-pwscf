#!/usr/bin/env python3

def li_to_str(li):
  s = ""
  for thing in li:
    s += str(thing)
    if not str(thing).endswith('\n'):
      s += '\n'
  return s

def str_to_li(st):
  return st.split('\n')
  

def float_if_number(var):
  try:
    return float(var)
  except ValueError:
    return str(var)

def format_pair(var_str, val_str):
  if type(float_if_number(val_str)) == float:
    return "{}={}".format(var_str, val_str)
  else:
    return "{}='{}'".format(var_str, val_str)


class Namelist(object):
 
  def __init__(self, name = "unamed", content_init = [] ):
    uppercase = [
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
    
    self.content = content_init
    self.name = name
    if self.name not in valid_namelists:
      raise ValueError('{} is not a valid namelist.'.format(self.name))
        
    
  def __str__(self):
    return '\t&{}\n{}{}'.format(self.name, li_to_str(self.content),'/')

  def __repr__(self):
    return self.__str__()
 
  def add_variable(self, var, val):
    self.content.append(format_pair(var, val))

  
  def get_index(self, var):
    return self.content.index(var)



def main():
  control_namelist = ["title='scf-HMX-792927'", 
"prefix='scf.pbe-n-kjpaw.ec-80.kp-444'",
"calculation='scf'",
"verbosity='high'",
"restart_mode='restat'",
"nstep='200'",
"pseudo_dir='/users/majewski/.data/PSEUDOPOTENTIALS'",
"outdir='./scratch/'",
"tstress='.true.'",
"tprnfor='.true.'",
"wf_collect='.false.'",
"forc_conv_thr=1.0e-4"]

  print("control_namelist:",li_to_str(control_namelist))
  print("Add another variable to the namelist:")
  var = input("variable name:\t")
  val = input("value of variable:\t")
  print(
    "We will add this line:\n{}".format(format_pair(var,val))
    )
  control_namelist.append(format_pair(var, val))
  print("li is now:\n\t{}".format(control_namelist))

 
     
      
