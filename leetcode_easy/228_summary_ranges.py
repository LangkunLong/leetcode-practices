class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []

        result = []
        start = nums[0]
        end = nums[0]

        # instead of making range go over bound, can just check the last element at the end
        for i in range(1, len(nums)):
            if end + 1 != nums[i]:
                interval = ""
                if start == end:
                    interval = str(start)
                else:
                    interval = str(start) + "->" + str(end)
                result.append(interval)
                start = nums[i]
            end = nums[i]
        
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{end}")
        return result
