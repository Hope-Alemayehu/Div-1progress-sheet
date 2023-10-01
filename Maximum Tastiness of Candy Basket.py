class Solution(object):
    def maximumTastiness(self, price, k):
        """
        :type price: List[int]
        :type k: int
        :rtype: int
        """
        #sort the list of candy prices in ascending order
        price.sort()

        #helper function
        def good(target):
            #candy represent the number of candies
            candy = 0
            #represent the price of previously selected candy
            last = -10**20

            #iterates over each candy's price in the price list
            for x in price:
                #checks if the difference between current candy price and previous candy price >= to tar
                if x - last >= target:
                    candy += 1
                    last = x
                if candy >= k:  # Early termination if enough candies are selected
                    break
            #checks if the number of candies equal to k
            return candy >= k

        #represent minimum possible tastiness
        left = 0
        #maximum level of tastiness
        right = 10**12


        while left < right:
            #calculate the mid point and rounding it to nearest integer
            mid = (left + right + 1) // 2
            
            if good(mid):
                left = mid
            else:
                right = mid - 1

        return left
