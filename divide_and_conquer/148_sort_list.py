# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        cur = head
        head_list = []
        while cur:
            head_list.append(cur.val)
            cur = cur.next
        head_list_sort = sorted(head_list)
        #print(head_list_sort)

        def helper(l, r):
            if l > r:
                return None
            node = ListNode(head_list_sort[l])
            node.next = helper(l + 1, r)
            return node
        
        res = helper(0, len(head_list_sort)-1)
    
        return res
