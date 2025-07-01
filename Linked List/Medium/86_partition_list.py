# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        # create 2 lists
        left, right = ListNode(), ListNode()
        l_end, r_end = left, right
        while head:
            if head.val >= x:
                r_end.next = head
                r_end = r_end.next
            else:
                l_end.next = head
                l_end = l_end.next
            head = head.next
        l_end.next = right.next
        r_end.next = None
        
        return left.next