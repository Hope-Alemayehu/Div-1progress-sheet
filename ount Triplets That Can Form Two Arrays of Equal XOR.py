from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        #time complexity=O(N^2)
        #space complexity=O(n)
        n = len(arr)
        prefix_xor = [0] * (n + 1)  # Initialize prefix XOR array
        count = 0  # Initialize count of triplets

        # Calculate prefix XOR array
        for i in range(1, n + 1):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]

        # Iterate over all possible pairs (i, k)
        for i in range(n - 1):
            for k in range(i + 1, n):
                # Calculate XOR value for a
                a = prefix_xor[k + 1] ^ prefix_xor[i]

                # Check if a == 0 and increment count by (k - i)
                if a == 0:
                    count += (k - i)

        return count
