class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # re-doing this question, first sort using start indices, so we have intervals in increasing order
        # if the start index of second interval <= end index of first interval, update end interval to max(e1, e2)

        intervals = sorted(intervals, key=lambda x:x[0])
        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            start, end = interval[0], interval[1]
            cur_end = res[-1][1]

            if start <= cur_end:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append(interval)
        return res
            
                
