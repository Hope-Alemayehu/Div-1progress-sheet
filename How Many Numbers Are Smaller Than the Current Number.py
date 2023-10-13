class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<2:
            retrun ( nums)
        nSorted=sorted(nums)
        res=[]
        for num in nums:
            idx=nSorted.index(num)
            res.append(idx)
        return res
