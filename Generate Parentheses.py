class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        combinations = set()
        self.generate("", 0, 0, n, combinations)
        return combinations

    def generate(self, current, open, close, n, combinations):
        if open == n and close == n:
            combinations.add(current)
        if open < n:
            self.generate(current + "(", open + 1, close, n, combinations)
        if close < open:
            self.generate(current + ")", open, close+ 1, n, combinations)
