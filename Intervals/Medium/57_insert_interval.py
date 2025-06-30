class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        new_start, new_end = newInterval[0], newInterval[1]

        import bisect

        def get_key(row):
            return row[0]
        
        class KeyWrapper:
            def __init__(self, array, key):
                self.array = array
                self.key = key
            def __getitem__(self, index):
                return self.key(self.array[index])
            def __len__(self):
                return len(self.array)
            
        # binary search to find entry
        wrapped_array = KeyWrapper(intervals, key=get_key)
        insert_index = bisect.bisect_left(wrapped_array, new_start)
        intervals.insert(insert_index, newInterval)
    
        # merge intervals
        local_min = intervals[0][0]
        local_max = intervals[0][1]
        merged_interval = []
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start > local_max: 
                merged_interval.append([local_min, local_max])
                local_min = start
                local_max = end
            local_min = min(start, local_min)
            local_max = max(end, local_max)
        merged_interval.append([local_min, local_max])

        return merged_interval

