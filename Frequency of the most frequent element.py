class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        #time compecity O(Nlogn)
        #space complexity O(1)
        #approch :sliding window 
        nums.sort()
        count=0
        l=0
        orgsum=0
        for r in range(len(nums)):
            orgsum += nums[r]

            while orgsum + k < (r - l + 1) * nums[r]:
                orgsum -= nums[l]
                l += 1

            count = max(count, r - l + 1)

        return count
