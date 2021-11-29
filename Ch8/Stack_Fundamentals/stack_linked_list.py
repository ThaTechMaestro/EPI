'''
Common patterns to linkedlist:
    Use of a temporary variable/single pointer
    Use of two or more temporary variable/multiple pointers
        This is due to the absence of a mechanism of accessing individual elements
        in the linkedlist, like arrays

Wrong Assumptions I made:
    Thinking the first elemement in the stack is the head(The stack is a pointer
        or reference variable to the first element in a stack)
    Thinking the Head is a starting Node (It is not, it is a pointer to the starting node)

Edge Cases:
    For each operation, always check if the stack is empty
    Ensure the links are pointing to the current elements

'''

class EmptyStackError():
    pass

class Node:

    def __init__(self, value):
        self.value = value
        self.link = None 


# Implementation of a stack using linkedlist    
# In visualising the implementation
# The head is not a node but a reference variable or a starting point
#   It serves as a pointer to the most recently added node to the the stack 
class Stack:

    def __init__(self):
        self.head = None

    
    # We then proceed to define the logic for the different operation 
    # In a stack
    
    def is_empty(self):
        return self.head == None
    

    def size(self):
        if self.head == None:
            return 0

        count = 0
        p = self.top
        while p is not None:
            count+=1
            p=p.link

        return count


    def push(self, data):
        if self.head == None:
            self.head = Node(data) 
        else:
            temp = Node(data)
            temp.link = self.head
            self.head = temp  
    
    def pop(self):

        if self.is_empty():
            raise EmptyStackError("Stack is empty")

        popped_element = self.top
        self.top = self.top.link

        return popped_element.value
    
    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")

        peeked_element = self.head
        return peeked_element.value
    
    def display_stack(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
            return
        print("Stack is:  ")
        Node = self.head

        while Node is not None:
            print(" ", Node.value)
            Node = Node.link

#----------------------------------------------------------
# Test Operations
if __name__ == '__main__':
    st = Stack()

    while True:
        print()

 

    




