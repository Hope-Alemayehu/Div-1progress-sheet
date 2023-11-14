class Solution:
    def minWindow(self, s: str, t: str) -> str:
       #given two strings s and t with length m and n

        # return the minimum window substring of s such that every character in t is included in the window
        #if there is no such string return ""
        #time complexity =O(N)
        #space complexity=O(N)
        #approch: sliding window
        countT,window={},{}
        for c in t:
            countT[c]=1+countT.get(c,0)
        
        res=[] #to store the in index of the answer
        reslen= float("infinity") #to store the minimum length of the string
        l=0
        have=0
        need=len(countT)
        for r in range (len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)

            if c in countT and window[c]==countT[c]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        
        if reslen != float("infinity"):
            l , r= res
            return s[l:r+1]
        else:
            return ""

        
