class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # is interval being given to me in increasing order? or do I need to sort 
        # can sort using the inner list and the start interval
        # need to keep track of global min and max 

        result = []
        intervals.sort(key=lambda x: x[0])
        local_min = intervals[0][0]
        local_max = intervals[0][1]
        #print(intervals)
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            # not contiguous 
            if start > local_max:
                result.append([local_min, local_max])
                # reset bounds 
                local_min = float(inf)
                local_max = 0
            local_min = min(start, local_min)
            local_max = max(end, local_max)

        # add in the last interval 
        result.append([local_min, local_max])
        return result 
            
                