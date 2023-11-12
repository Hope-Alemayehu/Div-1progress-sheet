class Solution:
    def calPoints(self, ops: List[str]) -> int:
       #time complexity O(N)
        #space complexity O(N)
        #approch: stack , basic conditional statments
        
        stack=[]
        for i in range(len(ops)):
            if ops[i]=="+":
                stack.append(stack[-1]+stack[-2])
            elif ops[i]=="D":
                stack.append(stack[-1]*2)
            elif ops[i]=="C":
                stack.pop()
            else:
                stack.append(int(ops[i]))
        return (sum(stack))
