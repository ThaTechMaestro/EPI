'''
https://leetcode.com/problems/search-insert-position/


'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
#--------------------------------------------------------------------------------------------------------------
        '''
        Brute force approach:
            Time complexity: O(n)
            Space Complexity: O(1)
        '''
        for i in range(len(nums)):
            
            
            #target is not the last element in nums
            if nums[i] > target and target in nums:
                return (i-1)
            
            #target as the last element in nums
            if nums[i] == target and target in nums:
                return (i)
                  
            #if target existed it would be among nums element, so you return its index f it existed
            if nums[i] > target and target not in nums:
                return (i)
            
            #if target existed would have been an addition to the last element in nums
            if nums[-1] < target and target not in nums:
                return (len(nums))
            
            
            if nums[0] < target and target not in nums and len(nums) == 1:
                return (len(nums))

#-------------------------------------------------------------------------------------------------------------------------------------------------
        '''
        Optimal approach:
            Time complexity: O(logn)
            Space Complexity: O(1)

        Very nice question:
            Is the array sorted?
                If it is, check Binary search
        '''
        
        left_pointer, right_pointer = 0, len(nums)-1

        while left_pointer <= right_pointer:
            
            middle_pointer = left_pointer+right_pointer//2

            if target == nums[middle_pointer]:
                return middle_pointer
            
            if target > nums[middle_pointer]:
                left_pointer = middle_pointer + 1
            else:
                right_pointer = middle_pointer - 1
        
        return left_pointer







            