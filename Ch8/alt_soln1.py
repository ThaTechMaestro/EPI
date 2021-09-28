def is_valid(s):

    # An odd numbered input means it is invalid
    if len(s) % 2:
        return False
    
    closed = {'(':')', '{':'}', '[':']'}
    stack = ['']

    for bracket in s:
        if bracket in closed:
            stack.append(closed[bracket])
        
        elif bracket != stack.pop():
            return False 
    
    return stack == ['']
    