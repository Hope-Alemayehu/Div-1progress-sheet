class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        N = len(arr)
        output = []

        for i in range(N, 1, -1):  # We need to sort elements from N to 1
            max_ = arr.index(i)  # Find the index of the largest element

            if max_ != i - 1:
                # If the largest element is not at the right position (i - 1),
                # flip it to the beginning and then flip it to its correct position
                if max_ != 0:
                    output.append(max_ + 1)
                    self.flip(arr, max_)

                output.append(i)
                self.flip(arr, i - 1)  # Subtract 1 to stay within valid index range

        return output

    def flip(self, arr, end):
        start = 0
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
