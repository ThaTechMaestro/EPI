# Alternative Best Solution

'''
Mistake insight:
    Watch how you intialise your stack
        either it is empty or with a first element
'''

def is_valid(s):

    '''
    An odd numbered parenthesis means
    it can not be balanced, hence it is invalid
    '''
    if len(s) % 2:
        return False
    
    # Storing matching open and close parenthesis in a dictionary
    closed = {'(':')', '{':'}', '[':']'}

    #A stack with a single element
    stack = ['']


    '''
    Since our string input has a minimum value of 1:
        We can skip the test case of an empty input
        --but a great edge case will be when there is an empty input --> return true

        We loop through our input performing different test for validity
            as conditions   
    '''
    for bracket in s:

        '''
        If an individual element in the input string is an open parenthesis/bracket
            store the matching closing parentheis/bracket in the stack
        '''
        if bracket in closed:
            stack.append(closed[bracket])

        elif bracket != stack.pop():
            '''
            If an individual element in the input string is a closing parenthesis/bracket
            check if it matches the last element stored in the stock
            if it does not, input is invalid
            '''
            return False 
    
    '''
    If the stack is empty, then the input is valid, else invalid
    '''
    return stack == ['']
