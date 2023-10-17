class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        #two pointers that moves inward
        left=0
        right=len(plants)-1
        refil=0

        #not to loss alice and bobs capacity
        currA=capacityA
        currB=capacityB

        #to iterate throught the list
        while left < right:
            #checks if the current Alice's capacity is less that the plant 
            if currA <plants[left]:
                currA=capacityA
                refil+=1
            #if the current alice's capacity > plants 
            currA-=plants[left]
            left+=1

            #checks if the current Bob's capacity is less that the plant 
            if currB<plants[right]:
                currB=capacityB
                refil+=1
            #if the current bob's capacity > plants 
            currB-=plants[right]
            right-=1
            #if left and right are equal or in the middle
            if left==right:
                #take max of alice;s or bob;s capacity
                cur=max(currA,currB)
                if cur < plants[left]:
                    refil+=1
        return refil
