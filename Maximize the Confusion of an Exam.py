class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # left=0
        # right=left+1
        # count=k
        
        # res=[]
        # for right in range (len(answerKey)):
        #     lenkey=0
        #     while answerKey[left]==answerKey[right]:
        #         lenkey+=1
        #         right+=1
        #     if answerKey[left]!=answerKey[right] and count>0:
        #         lenkey+=1
        #         right+=1
        #         count-=1
        #     elif answerKey[left]!=answerKey[right] and count==0:
        #         left+=1
        #     res.append(lenkey)
        # return max(res)

        left=0
        size=len(answerKey)
        ans=0
        count=0

        for i in range(size):
            if answerKey[i]=='F':
                count+=1
            while count>k:
                if answerKey[left]=='F':
                    count-=1

                left+=1
            ans=max(i-left+1,ans)  
        left=0 
        count=0
        for i in range(size):
            if answerKey[i]=='T':
                count+=1
            while count>k:
                if answerKey[left]=='T':
                    count-=1

                left+=1
            ans=max(i-left+1,ans)     
        return ans
