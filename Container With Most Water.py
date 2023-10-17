class Solution:
    def maxArea(self, height: List[int]) -> int:
        #brute force techniques
        #time complexity o(n*2)
        # res=0
        # for left in range(len(height)):
        #     for right in range(left+1,len(height)):
        #         area=(right-1)* min(height[left],height[right])
        #         res=max(res,area)
        # return res


    #time complexity= o(N
    #space complexity=o(1) because it uses constant space
        res=0
        left=0
        right=len(height)-1
        
        while left<right:
            area= (right-left)* min(height[left],height[right])
            res=max(res,area)
            
            if height[left]<height[right]:
                left+=1
            # elif height[left]>height[right]:
            #     right-=1
            else :
                right-=1
        return res



        
