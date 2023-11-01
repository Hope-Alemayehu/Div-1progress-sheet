class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
       #time complexity=O(N)
       #space complexity O(k)
        count=[0]*k
        sum=0

        for num in nums:
            sum+=num%k
            count[sum%k]+=1
        res=count[0]
        for c in count:
            res+=c*(c-1)//2
        return res
