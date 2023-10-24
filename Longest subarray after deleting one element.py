class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
      #time complexity=O(N)
      #space complexity=O(1)
        k=1
        l,r=0,0
        for r in range(len(nums)):
            if nums[r]==0:
                k-=1
            
            if k<0:
                k+=nums[l]
                l+=1
        return r-l
