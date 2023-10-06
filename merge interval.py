class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)<=1:
            return intervals
        intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time
        
        merged = []
        n = len(intervals)
        i = 0
        
        while i < n:
            current_begin, current_end = intervals[i]
            
            if i == n - 1:
                merged.append([current_begin, current_end])
                break
            
            next_begin, next_end = intervals[i + 1]
            
            if current_end < next_begin:
                # If the current interval does not overlap with the next interval,
                # add it to the merged list.
                merged.append([current_begin, current_end])
                i += 1
            else:
                # If the current interval overlaps with the next interval,
                # merge them by updating the end time of the current interval.
                intervals[i + 1][0] = current_begin
                intervals[i + 1][1] = max(current_end, next_end)
                i += 1
        
        return merged
