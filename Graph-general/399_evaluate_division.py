class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # using a dfs approach, because each node cannot find immedidate path with just 
        # its neighbors, have to traverse all available nodes
        # assume input always valid

        # DFS approach: 
        # thinking of using an iterative stack, keep track of visited 
        from collections import defaultdict

        adj_map = defaultdict(list)
        res = []

        # construct double edge adjacency graph
        for i in range(len(equations)):
            fwd_value = values[i]
            back_value = 1 / fwd_value

            src, dst = equations[i][0], equations[i][1]
            adj_map[src].append((dst, fwd_value))
            adj_map[dst].append((src, back_value))
            print(adj_map)

        # query logic, if nodes don't exist in the graph, return -1
        for i in range(len(queries)):
            src, dst = queries[i][0], queries[i][1]
            found = False
            print(src, dst)
            if src in adj_map and dst in adj_map:
                # dfs
                visited = set()
                dfs_stack = []
                dfs_stack.append((src, 1))                
                
                while(dfs_stack):
                    cur = dfs_stack.pop()
                    node, val = cur[0], cur[1]
                    visited.add(node)
                    if node == dst:
                        found = True
                        res.append(val)
                        print(src, dst, val)
                        break

                    # python list pops from the back, to have the behaviour as 
                    # recursive dfs to pop from the front, need to reverse node list
                    for neigh in reversed(adj_map[node]):
                        nxt_node, nxt_val = neigh[0], neigh[1]
                        if nxt_node not in visited:
                            dfs_stack.append((nxt_node, val * nxt_val))
                if not found:
                    res.append(-1.0)                 
            else:
                res.append(-1.0)

        return res


