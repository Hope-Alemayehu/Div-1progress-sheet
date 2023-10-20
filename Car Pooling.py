class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        #time complexity = O(2N)
        #space complexity=O(N)
        passengercount=[0]*1001

        for trip in trips:
            passenger,start,end=trip
            passengercount[start] +=passenger
            passengercount[end]-=passenger
            
        usedcapacity=0

        for count in passengercount:
            usedcapacity+=count
            if usedcapacity>capacity:
                return False
        return True
