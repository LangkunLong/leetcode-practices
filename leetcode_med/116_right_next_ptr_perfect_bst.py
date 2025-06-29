class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # everything is balanced, so don't have to worry about checking for null
        if not root:
            return None
        cur_node = root
        nxt_node = cur_node.left
        while cur_node and nxt_node:
            while cur_node:
                cur_node.left.next = cur_node.right
                if cur_node.next:
                    cur_node.right.next = cur_node.next.left
                cur_node = cur_node.next
            cur_node = nxt_node
            nxt_node = nxt_node.left
        return root