class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            minIdx=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[minIdx]:
                    minIdx=j
                    
            nums[i],nums[minIdx]=nums[minIdx],nums[i]
                   
        return nums
    
