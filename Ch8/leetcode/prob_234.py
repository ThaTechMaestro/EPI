'''

Continue from here:https://www.youtube.com/watch?v=yOzXms1J6Nk
    Timestamp: 8:52

Palindrome Linked List:
    This can be solved using Stacks or Two pointers

Link: https://leetcode.com/problems/palindrome-linked-list/discuss/64689/Python-easy-to-understand-solution-with-comments-(operate-nodes-directly).

How do  I check if something is a palindrome?
But for linkedlist I can not access the tail


Linked List do not permit accessing elements,
    hence the last element of the linked list can not be accessed
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        

        """
        :type head: ListNode
        :rtype: bool

        Using two pointers
        """

#------------------------------------------------------------------------------------------------------------->>>>>>
        '''
        Naive  Solution using an array to utilise indexing(Converting Linkedlist to an array question)

        Strategy: Using two pointers utilising the strength of an array via indexing:
                    Left pointer is placed beginning of an array
                    right pointer is placed at the end of the  array

        Mistake Code pieces:
                    while left_pointer != right_pointer:
                        if nums[left_pointer] != nums[right_pointer]:
                            return False
            
                        left_pointer += 1
                        right_pointer -= 1
                    
                    This piece of code above is wrong as the while loop conditions 
                    assumes you are only dealing with odd numbered length of strings
                    but what about even numbered, where they do not have an intersecting element?
        
        
        Since the memory defined (an array) is within a single loop,
        As the defined memory depends on the number of elements added to the memory

        The memory is not constant or clearly defined from the onset

        Time Taken: 33mins


        '''

        nums = []

        while head:

            nums.append(head.val)
            head = head.next

        
        left_pointer = 0
        right_pointer = len(nums) -1

        while left_pointer <= right_pointer:
            if nums[left_pointer] != nums[right_pointer]:
                return False
            
            left_pointer += 1
            right_pointer -= 1
        
        return True


#------------------------------------------------------------------------------------------------------------->>>>>>

        '''

         Naive  Using two pointers (Fast and slow)

        Strategy: 

        Mistake Code pieces:
                    
        
        
        Constant memory means using the given data structure with no extra addition of space added

        Question:
            We have the 
                the beginning node in the list
                the middle or almost middle
                the end node in the list
            
            We can then keep using the beginning and end node to
                check if it is a palindrome
            
            What is the purpose of the slow pointer node?

        Time Taken: 


        '''

        fast = head 
        slow = head 



        # Find middle (using slow pointer)
        while fast and fast.next:
            '''
            The condition above helps the fast pointer always point to
                the last node in the list
            It points to the last value node in the list if there is an 
                odd number of element in the list
            It points to the None node in the list if there is an even
                number of element in the list, converting the even numbered element in the 
                list to an odd number of element in the list

            --> The approach for converting it to an odd numbered list works, because it has a middle
                hence when there is a middle in a palindrome, we can compare left and right consecutive
                elements and determine if it is palindromic or not.
            '''


            fast = fast.next.next
            slow = slow.next
        
        # reverse second half

        prev = None

        #Look through reversing a linkedlist again(understand this), get the the reversing a linkedlist picture right
        while slow:
            temp = slow.next
            slow.next = prev 
            prev = slow
            slow = temp 
      


        












#------------------------------------------------------------------------------------------------------------->>>>>>



