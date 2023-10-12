class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """

        piles.sort()
        total = 0
        i = len(piles) - 2
        t = len(piles) / 3
        j = 0
        while j < t:
            total += piles[i]
            i -= 2
            j += 1
        return total


        
