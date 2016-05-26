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
        self.content = []
    else:
        if type(content) != list:
          raise TypeError("Namelist(name=\"\", content=None)\n\tIf content is not None, content must be of type list")
        self.content = content

    if self.name not in valid_namelists:
      raise ValueError('{} is not a valid namelist.'.format(self.name))
        
    
  def __str__(self):
    return '\t&{}\n{}{}'.format(self.name, li_to_str(self.content),'/\n')

  def __repr__(self):
    return self.__str__()
 
  def set_value(self, var, val):
    self.content.append(format_pair(var, val))

  def set_multiple(self, var_list, val):
    for var in var_list:
      self.set_value(var, val)
  
  def get_index(self, var):
    return self.content.index(var)

