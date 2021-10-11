'''
Problem Link: https://leetcode.com/problems/min-stack/

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
        
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()