class Solution:
    def scoreOfParentheses(self, s: str) -> int:
      
        #STACK SOLUTION
        # stack = []
        # score = 0

        # for c in s:
        #     if c == "(":
        #         stack.append(score)
        #         score = 0
        #     else:
        #         score = stack[-1] + max(score * 2, 1)
        #         stack.pop()

        # return score

        #TWO POINTERS SOLUTION
        left = 0
        score = 0

        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                left -= 1
                if s[i-1] == "(":
                    score += 2 ** left

        return score
