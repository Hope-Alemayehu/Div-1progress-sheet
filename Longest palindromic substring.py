class Solution:
    def longestPalindrome(self, s: str) -> str:
        #give a string
        #goal to return the longest palindromic substring in s
        #palindromix means it reads the same forward and backward
        
        #time complexity=O(N^2)
        #space complexity=O(1)
        res= ""
        reslen=0

        for i in range(len(s)):
            #odd length
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:
                    res=s[l:r+1]
                    reslen=r-l+1
                l-=1
                r+=1
                
            #even length
            l,r=i,i+1
            while l>=0 and r<len(s)and s[l]==s[r]:
                if (r-l+1)>reslen:
                    res=s[l:r+1]
                    reslen=r-l+1
                l-=1
                r+=1
        return res

        
