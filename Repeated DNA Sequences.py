class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #time complexity=O(N)
        #space complexity=O(N)

        seen,res=set(),set()
        for l in range(len(s)-9):
            cur=s[l:l+10]
            if cur in seen:
                res.add(cur)
            seen.add(cur)
        return res
