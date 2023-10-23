class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #time complexity  o(N)
        #space complexity O(1)
        curSum=0
        sumMax=nums[0]

        for n in nums:
            if curSum<0:
                curSum=0
            curSum+=n
            sumMax=max(curSum,sumMax)
        return sumMax
        
