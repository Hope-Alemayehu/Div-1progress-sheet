class DataStream:
    
    #the problem is we have integers
    #we need to write a consec methood to check sth
    #we are given value and k
    #value is the amount of that integer
    #k is the number of integer in the back we need to consider when we check consecativeness
    #consec methood is used to check if the last k element is equal to the vale
    def __init__(self, value: int, k: int):
        self.value=value
        self.count=0
        self.k=k

    def consec(self, num: int) -> bool:
        if num==self.value:
            self.count+=1
            return self.count>=self.k

        self.count=0
        return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
