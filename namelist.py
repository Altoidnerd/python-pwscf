#!/usr/bin/env python3

def float_if_number(var):
  try:
    return float(var)
  except ValueError:
    return str(var)

def format_val(val):
  if type(float_if_number(val)) == float:
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



