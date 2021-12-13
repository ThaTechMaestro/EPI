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

        Time Complexity: O(n)
        Space Complecity: O(n)


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


        Personalised interpretation for fast and slow pointers
            For every number of steps made by the slow pointer from the starting point
            The fast pointer makes twice the number of those steps
                Hence these favors even number of nodes in a linked list
                In cases of odd number of nodes in a linked list, the use of None object is used  to make  it even numbered,
                    hence the slow pointer always points to the  middle of the node


        STRATEGY:
            It is using a linkedlist
            The actual test for palindrome involves the use of indexes and values:
                Using two pointers, compare the values of their index start at the extreme ends (far left and far right indices)
                Since this is a linked list
                    We use fast and slow pointers to get the mid node and last node
                    The purpose of mid node is to aid the test for palindrome, since it involves comparison from two opposite extreme postions
                        and we are using a singly linked list
                    We would have to reverse the second half of the linked list
                        Then perform the actual test for palindrome
                            It is this long since linkedlist uses pointers, hence we have to rearrange the structure to apply the algorithm

            Summary:    
                Rearrange the linkedlist structure then apply the palindrome test/algorithm on it. 

                    Palindrome algorithm:
                        Compare the values of the extreme opposite indices (left and right indices) on the specified data structure
                            If they match before they cross paths or point to an intersecting value, hence it is a palindrome

        Mistake Code pieces:
                    
        
        
        Constant memory means using the given data structure with no extra addition of space added

        Question:
            We have the 
                the beginning node in the list
                the middle or almost middle
                the end node in the list
            
            We can then keep using the beginning and end node to
                check if it is a palindrome (Nope, this is to alter the structure to suit the application of the required algorithm)
            
            What is the purpose of the slow pointer node?
                To point to the mid node and help with reversal

        Time Complexity: O(n)
        Space Complecity: O(n)


        '''


        '''
        Get the Middle Node
        Let it point to None
        '''
        fast = head 
        slow = head 
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
        
        
        '''
        Reverse the left half of the linked list
        '''
        prev = None
        while slow:
            temp = slow.next
            #Actual reversal
            slow.next = prev 

            prev = slow
            slow = temp 


        #Test For palindrome
        left_pointer = head
        right_pointer = prev 
        while right_pointer:

            if right_pointer.val != left_pointer.val:
                return False 
            
            left_pointer = head 
            right_pointer = prev 
        
        return True



'''

Last discussion to be reviewed:
https://leetcode.com/problems/palindrome-linked-list/discuss/64689/Python-easy-to-understand-solution-with-comments-(operate-nodes-directly).
'''


        












#------------------------------------------------------------------------------------------------------------->>>>>>

