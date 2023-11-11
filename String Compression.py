class Solution:
    def compress(self, chars: List[str]) -> int:
        #chars is the array of characters
        #return the last index after compressing 
        #the compressed string should be modified in the input array
        #return the length of the new array
        #no extra space

    #how i am going to solve this 
    #use 3 variable one i,index,j :i to iterate throught the arr index to modify the array
    #j to find those of the same characters

        #time complexity = O(N)
        #space complexity=O(1)
        #approches two pointers
        i=0
        index=0
        count=0
        while i<len(chars):
            count=0
            j=i
            while j<len(chars) and chars[i]==chars[j]:
                count+=1
                j+=1
            chars[index]=chars[i]
            index+=1

            if count>1:
                for c in str(count):
                    chars[index]=c
                    index+=1
                
            i=j
        chars=chars[:index]
        return index
