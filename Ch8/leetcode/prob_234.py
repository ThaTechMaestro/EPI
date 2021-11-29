'''

Palindrome Linked List:
    This can be solved using Stacks or Two pointers


How do  I check if something is a palindrome?
But for linkedlist I can no access the tail

'''

class Solution(object):
    def isPalindrome(self, head):
        

        """
        :type head: ListNode
        :rtype: bool

        Using two pointers
        """


        slow = head
        fast = head


        # Find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next 
        

        # Reverse the second half
        node = None 


        while slow:
            nxt = slow.next
            slow.next = node 
            node = slow 
            slow = nxt 
        

        while node:
            if node.val != head.val:
                return False 
            node = node.next
            head = head.next
        

        return True 

        
