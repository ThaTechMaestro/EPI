'''

Why can you print individual elemements 
  in a python string?

What amazes me is 

  why did they use a dictionary for
    key value access of opening and 
    corresponding parenthesis

  Why is a dictionary unordered?
    In dictionary we loop through the keys

  8.3 in EPI

'''

'''
For structures in Python:
Normal Evaluation
Is it initialised? - True (Proceed)
or
Is it empty? - False (Proceed)

Not -- Changes the structure 
It evaluates the Normal False statement
and neglects the Normal True statement

Is it empty ? - True

Is it initialised ? - False

------------------------------
  
'''


'''
a = []

if not a:
  print(True)
else:
  print(False)

'''



#------------------------------
#Style 1
def is_well_formed(s):

  open_symb_store = []

  lookup = {'(':')', '{':'}', '[':']'}

  for symbol in s:
    if symbol in lookup:
      open_symb_store.append(symbol)
    elif not open_symb_store or lookup[open_symb_store.pop()] != symbol:
      return False 
  
  return not open_symb_store

#-----------------------------------------
# Style 2
def is_well_formed(s):

  open_symb_store = []

  lookup_table = {'(':')', '{':'}', '[':']'}

  for symbol in s:
    if symbol in lookup_table:
      open_symb_store.append(symbol)
    elif lookup_table[open_symb_store.pop()] != symbol:
      return False
    elif not open_symb_store:
      return False 
  
  return not open_symb_Store

#-------------------------------------------------
#Style 3
def is_well_formed(s):

  open_symbol_store = []
  lookup_table = {'(':')', '{':'}', '[':']'}

  for symbol in s:

    if symbol in lookup_table:
      open_symbol_store.append(symbol)
    elif symbol == lookup_table[]






