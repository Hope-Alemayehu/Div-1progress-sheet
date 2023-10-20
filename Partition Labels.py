class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #time complexity O(2n)=O(N)
        #space complexity O(26)=O(1)

        #creat a hashmap
        #use enumerate to match each character with their last index
        #res
        #initalize start and end
        #enumerate index and characters while incresing the size
        #put stoping criteria
        
        lastidx={}

        for i ,c in enumerate(s):
            lastidx[c]=i
        
        res=[]
        size=0
        end=0
        for i ,c in enumerate(s):
            size+=1
            end=max(end,lastidx[c])

            if i == end:
                res.append(size)
                size=0
        return res
