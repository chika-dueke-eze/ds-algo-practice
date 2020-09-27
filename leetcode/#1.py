class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums      #define parameters 
        self.target = target
        self.n = 0
        for i in self.nums:                 #iterate through the array
            newnums = self.nums[self.n+1:]  #get a new array of the values after the current value being iterated
            self.n += 1                     #update the value of n so as to reflect for the "new start" of the second array
            index1 = self.nums.index(i)     #get the first index of the value
            for x in newnums:               #iterate through the second array and use the add the initial value "i" with the all the next values after it in the array
                index2 = self.nums.index(x) #get second index
                if i+x == self.target:      #main part of the code, returns the indexes if we find two ums
                    return index1, index2
                else:
                    continue

##  ****SIMPLER VERSION ***
##
##def twoSum(nums, target):
##    
##    """
##    :type nums: List[int]
##    :type target: int
##    :rtype: List[int]
##    """
##    n = 0
##    for i in nums:
##        newnums = nums[n+1:]
##        n += 1
##        index1 = nums.index(i)
##        for x in newnums:
##            index2 = nums.index(x)
##            if i+x == target:
##                return index1, index2
##            else:
##                continue
##            
##if __name__ == "__main__":
##    print(twoSum([2,11,11,7], 9))
