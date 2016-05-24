

# a namelist begins with '&' character and ends with '/'
class namelist(object):
  def __init__(self, title, content):
    allowed_titles = [
      'CONTROL',
      'SYSTEM',
      'ELECTRONS']
    return '&{}\n{}\n{}'.format(title, content, '/')



class input_card(object):
  def __init__(self, title, title_parameter=''):
    self.title = title
    self.t_param = t_param
    self.content = content

    allowed_titles = [
      'CELL_PARAMETERS',
      'ATOMIC_SPECIES',
      'ATOMIC_POSITIONS',
      'K_POINTS']
]    
    if (title not in allowed_titles):
      raise NameError('title not a valid input_card')
    
    if self.title = 'ATOMIC_POSITIONS':
      pass
 
    def __repr__(self):
      return"{}  {}\n{}".format(title, title_parameter, content) 
