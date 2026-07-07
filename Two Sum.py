class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}  # dictionary to store value:index
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[nums[i]] = i
