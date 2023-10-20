class NumArray:
    #time complexity=O(N)
    #space complexity =O(n)
    def __init__(self, nums: List[int]):
        self.prefix=[]
        cur=0
        for n in nums:
            cur+=n
            self.prefix.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        # example [-2,0,3,-5,2,1]  left=2 right=5
        #rightsum=-1
        rightsum=self.prefix[right]
        if left>0:
            #leftsum [-2,0] =-2
            leftsum=self.prefix[left-1]
        else:
            leftsum=0
        #returns rightsum(-1)-leftsum(-2)=1 to check[3,-5,2,1] the sum of all this is 1
        return rightsum-leftsum
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
