class Solution:
    def connect(self, root: Optional[TreeNode]) -> None:
        # use a BFS traversal but we don't have to construct a queue, just need to traverse level by level and 
        # connect children together, stop when we don't have children to connect 
        # keep in mind that this is not a perfect tree, there will be missing nodes
        # use a dummy node to link the nodes in the level together, because certain level may not have a left node
        # also with a dummy node, can keep track of the previous node between 2 subtrees

        # general solution, using a BFS queue O(N) space
        from collections import deque
        
        if not root:
            return None
        
        level_list = deque()
        level_list.append(root)
        while level_list:
            num_nodes = len(level_list)
            dummy = TreeNode(0)
            # traverse all nodes on level
            while num_nodes != 0:
                cur_node = level_list.popleft() #nodes in the list can be either left child or right child
                dummy.next = cur_node
                dummy = dummy.next
                if cur_node.left:
                    level_list.append(cur_node.left)
                if cur_node.right:
                    level_list.append(cur_node.right)
                num_nodes -= 1
        return root
        
        # optimized solution using O(1) space, don't need to construct queue, just need to link nodes together
        # use a current and next pointer, next pointer point to the next level
        if not root:
            return None
        
        cur_node = root
        while cur_node:
            dummy = Node(0)
            temp = dummy
            # traverse all the nodes on the same level
            while cur_node:
                if cur_node.left:
                    temp.next = cur_node.left
                    temp = temp.next
                if cur_node.right:
                    temp.next = cur_node.right
                    temp = temp.next
                cur_node = cur_node.next
            cur_node = dummy.next
        return root