class Solution:
    def isValid(self, s: str) -> bool:
        #create stack
        #build a hash map to match th eopening and closing parentheses
        #use loop to iteraTE through the characters
        #use if statment to check if the character is in the hashmap
        #if it is use another if statment to check is the stack is not empthy and 
                #if the top of the stack matches with the hashmap value 
                #if yes we pop the top of the stack
        #else return false
        #use another if statment to check if ((( situation happens 
        #time complexity=O(N)
        #space complexity=O(N)

        stack = []
        closetoOpen = {"]": "[", "}": "{", ")": "("}

        for c in s:
            if c in closetoOpen:
                if stack and stack[-1] == closetoOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
