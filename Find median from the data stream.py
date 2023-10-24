class MedianFinder:
    #time complexity=o(nlogn)
    #space complexity=o(1)
    def __init__(self):
        self.num=[]

    def addNum(self, num: int) -> None:
        self.num.append(num)

    def findMedian(self) -> float:
        if not self.num:
            return None

        self.num.sort()
        k=len(self.num)//2
        median=0
        if len(self.num)%2==0 and k>0:
            median =(self.num[k]+self.num[k-1])/2
            return median
        else:
            return self.num[k]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
