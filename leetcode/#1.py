class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        complementMap = {}
        for idx, value in enumerate(nums):
            cmplment = target - value 
            if cmplment in complementMap:
                return [complementMap[cmplment], idx]
            
            complementMap[value] = idx
