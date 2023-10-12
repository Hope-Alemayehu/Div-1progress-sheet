class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #time complexity =O(nlogn) due to the sorting function being O(nlogn) and the loop being o(n)
        #space Complexity=o(n)
        if len(nums)<2:
            return 0
        nums.sort()
        maxDiff=[]
    
        for i in range (len(nums)-1):
            maxDiff.append(nums[i + 1] - nums[i])
        return max(maxDiff)
