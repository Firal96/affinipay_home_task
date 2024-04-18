from pydoc import locate

def match_structure(structure, response):
  try:
    for key, value in structure.items():
      if type(response[key]) is not locate(value):
        return False
    return True
  except:
    return False
  
def match_values(expected, response):
  try:
    for key, value in expected.items():
      if response[key] != value:
        return False
    return True
  except:
    return False