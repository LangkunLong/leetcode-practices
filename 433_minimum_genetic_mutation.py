class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        # using bfs approach to find min number needed
        # create directed, connected, graph, if cannot find entry, return -1
        from collections import defaultdict, deque
        adj_list = defaultdict(list)
        mutated = set()
        queue = deque()
        
        # step 1: construct graph using gene bank
        queue.append(startGene)
        while queue:
            base_gene = queue.popleft()
            mutated.add(base_gene)
            for mut_gene in bank:
                if mut_gene not in mutated:
                    if self.helper(base_gene, mut_gene) == 1:
                        adj_list[base_gene].append(mut_gene)
                        mutated.add(mut_gene)
                        queue.append(mut_gene)
        
        # step 2: traverse adjacency list finding endGene
        min_cost = float('inf')
        queue.clear()
        mutated.clear()
        queue.append((startGene, 0))
        # bfs
        while queue:
            cur = queue.popleft()
            mutated.add(cur)
            gene, path_cost = cur[0], cur[1]
            if gene == endGene:
                min_cost = min(min_cost, path_cost)
                break
            for next_mut_gene in adj_list[gene]:
                if next_mut_gene not in mutated:
                    queue.append((next_mut_gene, path_cost + 1))
        
        if min_cost == float('inf'):
            return -1
        else:
            return min_cost
                
    def helper(self, src, dst):
        # helper function to find number of mismatch chars between 2 genes
        mismatch = 0
        for i in range(len(src)):
            if src[i] != dst[i]:
                mismatch += 1
        return mismatch

#Example 1:

startGene = "AACCGGTT"
endGene = "AACCGGTA"
bank1 = ["AACCGGTA"]
Solution.minMutation(startGene, endGene, bank1)

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank2 = ["AACCGGTA","AACCGCTA","AAACGGTA"]
print(Solution.minMutation(startGene, endGene, bank2))