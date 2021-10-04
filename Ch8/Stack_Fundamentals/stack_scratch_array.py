class EmptyStackError(Exception):
      pass


class Stack:

  def __init__(self):
    self.items = []

  def is_empty(self):
    return self.items == []
    
  def size(self):
    return len(self.items)