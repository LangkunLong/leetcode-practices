class Solution:
    def candy(self, ratings: List[int]) -> int:
        # cannot sort, or else lose neignbor order
        # 2 traversals, one forward and one backward 
        # only consider adding if next element is bigger, otherwise can leave as 1 
        candys = [1 for _ in ratings]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candys[i] = candys[i-1] + 1 
        print(candys)
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                # also have to make sure that candies in the first traversal are not overwritten
                candys[i] = max(candys[i+1] + 1, candys[i])
        print(candys)
        return sum(candys)
        