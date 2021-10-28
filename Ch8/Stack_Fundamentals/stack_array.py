class EmptyStackError(Exception):
  pass


class Stack:

#--- Definition of attributes
#--- What are the properties which upon instantiation can make a stack object unique
  
  # The code below can be interpreted as
  # Upon creating a stack object it should have
  def __init__(self):
        
    #An internal array structure called Structure/Stack
    # Should be created
    self.structure = []


#--------------------------
#----Actions   

  def is_empty(self):
    return not self.structure

  def size(self):
    return len(self.structure)
  

  def push(self, element):
    return self.structure.append(element)

  def pop(self):
    if self.structure:
      return self.structure.pop()
    else:
      raise EmptyStackError("Stack is empty")


  def peek(self):
    if self.structure:
      return self.structure[-1]
    else:
      raise EmptyStackError("Stack is empty")

  def display(self):
    print(self.structure)

  def find_max(self):
    pass


if __name__ == '__main__':
  st = Stack()

  while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Size")
    print("5. Display")
    print("6. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
      x = int(input("Enter the element to be pushed: "))
      st.push(x)
    elif choice == 2:
      x = st.pop()
      print("Popped element is: ", x)
    elif choice == 3:
      print("Element at the top is: ", st.peek())
    elif choice == 4:
      print('Size of stack ', st.size())
    elif choice == 5:
      st.display()
    elif choice == 6:
      break
    else:
      print('Wrong choice')
    print()


