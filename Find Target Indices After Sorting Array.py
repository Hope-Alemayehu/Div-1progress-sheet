class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numS=sorted(nums)
        res=[]
        if len(nums)==0 :
            return []
       
        for i in range(len(nums)):
            if numS[i]==target:
                res.append(i)
        return res

