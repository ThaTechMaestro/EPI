'''
Problem Link: https://leetcode.com/problems/min-stack/
My Solution off the top of my head

One line explanation:
    Using loop to

Common Errors:
    - Forgetting to check if the stack is empty
    - You do not have to check if the stack is empty for push operations
    - Keeping track of the min_values, it should always start with the
        first element that gets pushed into the stack

Time Complexity: O(n)
Space Complexity: 

'''

class StackError(Exception):
    pass

class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        return self.stack.append(val)        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def top(self):
        """
        :rtype: int

        """
        
        if self.stack:
            return self.stack[-1]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        
        if self.stack:
            min_value = self.stack[-1]
            
            for i in self.stack:
                if min_value >= i:
                    min_value = i
                    
            return min_value
        else:
            return None
        

#------------------------------------------------------------------------------------------------------------    
'''
Alternative Solution1:
https://leetcode.com/problems/min-stack/discuss/747181/Clear-Python-code-faster-than-96

Initialisations
    - An empty stack
    - A variable serves as a placeholder for current min_value
    - Another empty stack for keeping previous min values

One Line explanation:
    The idea here is to keep track of min element using a separate stack

    Using two stacks to avoid iteration and performing operations in constant time.
    As seen in the code above, without an additional stack, we have to loop through

    Keep track of the minimum value when performing push and pop operations
        Logic for storing min value in a stack when performing a Push operation is simple
        Logic for storing min value in a stack when performing pop operation is a bit tricky, involves checking
            if the current min value is the one being popped
            and using a stack of previous min values
            to update the current min value 

It uses an extra data structure and performs operation in constant time
Time Complexity: O(1)
Space Complexity: 
'''


class MinStack(object):

    def __init__(self):
        self.stack = []
        
        self.min_value = float('inf')
        self.prev_min = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        
        if val <= self.min_value:
            self.prev_min.append(self.min_value)
            self.min_value = val
            

    def pop(self):
        """
        :rtype: None
        """
        if not self.stack:
            return None
        elif self.stack and self.min_value == self.stack[-1]:
                self.min_value = self.prev_min.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int

        """
        
        if self.stack:
            return self.stack[-1]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        
        if not self.stack:
            return None
        return self.min_value
        
        
#------------------------------------------------------------------------------------------------------------    
'''
Alternative Solution2: (Best Solution)
https://leetcode.com/problems/min-stack/discuss/572831/Python3-solution-with-O(1)-time-using-one-stack

Initialisations
    - An empty stack
    - A variable serves as a placeholder for current min_value

One Line explanation:
    It stores element in a stack as tuples (a,b),
        a represent element to be pushed or popped
        b represent the previous min value in the stack

It uses a single stack and performs operation in constant time
Time Complexity: O(1)
Space Complexity: 
'''




class MinStack:

  def __init__(self):

    self.stack = []

    self.current_min = float('inf')



  def push(self, x):

    if len(self.stack) == 0:
      self.stack.append((x,None))
      self.current_min = x
    else:
      # We only add previous min value as tuples with the current min value
      if x <= self.current_min:
        self.stack.append((x, self.current_min))
        self.current_min = x
      else:
        self.stack.append((x, None))
      
  
  def pop(self): 

    temp =  self.stack.pop()

    if temp[0] == self.current_min:
      self.current_min = temp[1]


    
  def top(self):
    return self.stack[-1][0]
    

    
  def getMin(self):
    return self.current_min