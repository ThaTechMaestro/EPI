'''
Name on Leetcode: Two Sum Problem

Identification: Sum Problem

array - nums 
int - target 
complement = {}


Loop through the array (using the index):
    if target - nums[i] == nums[i+1]:
        complement[i] = nums[i]




'''
def twoSum(self, nums, target):

    if not nums:
        return nums
    else:
        cache = {}

        for index, value in enumerate(nums):
            remainder = target - value 

            if remainder in cache:
                return [cache[remainder], index]
            else:
                cache[value]=index 

