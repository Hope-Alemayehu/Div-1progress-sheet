class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #time complexity O(2N) = O(N)
        #space complexity=O(N)
        stack1=[]
        stack2=[]
        for i in range(len(s)):
            if s[i]!="#":
                stack1.append(s[i])
            else:
                if len(stack1)!=0:
                    stack1.pop()
        for i in range(len(t)):
            if t[i]!="#":
                stack2.append(t[i])
            else:
                if len(stack2)!=0:
                    stack2.pop()
        return True if stack1==stack2 else False
