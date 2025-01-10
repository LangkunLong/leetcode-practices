class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # not similar to interval question, now need a precise point where intervals overlap 
        if not points:
            return 0
        # minimum 1 arrow needed, place arrow at end inverval to maximize popping the most balloons
        # if start point of new balloon is outside of end interval, we need a new arrow
        num_arrows = 1
        points.sort(key=lambda x: x[1])
        end_interval = points[0][1]
        for start, end in points[1:]:
            if start > end_interval:
                print(start, end)
                num_arrows += 1
                end_interval = end
        return num_arrows