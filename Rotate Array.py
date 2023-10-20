class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #time complexity O(3n)=o(n)
        #space complexity O(1)

        #to check if k is greater
        #[1,2,3,4,5,6,7] 
        k=k%len(nums)
        #to reverse the whole thing
        #[7,6,5,4,3,2,1]
        l,r=0,len(nums)-1
        self.reversed(nums,l,r)

        #to reverse from o to k elements,0-2 index
        #[5,6,7,4,3,2,1]
        l,r=0,k-1
        self.reversed(nums,l,r)

        #to reverse the rest 3-6 index
        #[5,6,7,1,2,3,4]
        l,r=k,len(nums)-1
        self.reversed(nums,l,r)
    def reversed(self,nums:List,l:int,r:int):
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
