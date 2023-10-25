class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #time complexity = O(N)
        #space complexity = o(N)
        #the look ups and comparision are o(1)time 
        if t=="":
            return ""
        
        #two hashmaps one to count,the other:
        countT,window={},{}
        
        #to map all teh character in t to countT map
        #the get function is to check if the character is in countT already
        for c in t:
            countT[c]=1+ countT.get(c,0)
        
        have,need=0,len(countT)
        #since we need the minimum we need to initalize it to maximum possible value infinity
        res,resLen=[-1,-1] ,float("inf")
        
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)

            #checking if c is in t and if their count of apperiance is equal
            if c in countT and window[c]==countT[c]:
                have+=1
            
            while have==need:
                #update the result
                if (r-l+1)<resLen:
                    res=[l,r]
                    resLen=(r-l+1)
                #to pop from the left to find the minumum length
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        #l:r+1 to include the right element
        return s[l:r+1]if resLen!=float("inf") else ""
