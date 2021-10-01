class Solution(object):
    def isValid(self, s) :
      stack = []
      length_of_input = len(s)

      for i in range(length_of_input):

        length_of_stack = len(stack)

        if not stack:
          stack.append(s[i])
        elif stack[length_of_stack - 1] == '(' and s[i] == ')':
          stack.pop(length_of_stack-1)
        elif stack[length_of_stack-1] == '{' and s[i] == '}':
          stack.pop(length_of_stack-1)
        elif stack[length_of_stack-1] == '[' and s[i] == ']':
          stack.pop(length_of_stack-1)
        else:
          stack.append(s[i])
    
      return not stack