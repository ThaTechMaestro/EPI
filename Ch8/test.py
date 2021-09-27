# https://leetcode.com/problems/valid-parentheses/discuss/1407199/EASY-SOLUTION-or-PYTHON-or-FATER-THAN-90-or-please-upvote
# Checking a new solution
# I will continue from here tommorow morning

def is_valid(s):
  stack = []
  length_of_symbol = len(s)

  for i in range(length_of_symbol):
    length_of_stack = len(stack)

    if length_of_stack == 0:
      stack.append(s[i])
    elif s[i] == ")" and stack[length_of_stack - 1] == "(":
      stack.pop(length_of_stack-1)
    elif s[i] == "}" and stack[length_of_stack - 1] == "{":
      stack.pop(length_of_stack - 1)
    elif s[i] == "]" and stack[length_of_stack - 1] == "[":
      stack.pop(length_of_stack - 1)
    else:
      stack.append(s[i])
    
    return len(stack) == 0
