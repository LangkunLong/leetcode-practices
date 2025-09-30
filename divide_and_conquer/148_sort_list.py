# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # using divide and conquer approach with merge sort
        # dividing down to a single node, then merging them together
        
        # with trees, linked lists, base case is always if null node
        # also for merge sort, return when we reach a single base node, or else mid would return always the same node
        # and we would keep calling sortList(left) and create an infinite loop
        # we want to return the single node
        if not head or not head.next:
            return head
        
        mid = self.getMid(head)
        # need to separate into 2 linked lists
        #print(mid.val)
        right = mid.next
        left = head
        mid.next = None

        s_left = self.sortList(left) # left to mid node
        s_right = self.sortList(right) # mid node + 1 to the end

        # now have single node
        merged_node = self.merge(s_left, s_right)
        return merged_node
        
    # helper to merge 2 sorted linked lists
    def merge(self, left, right):
        dummy = ListNode()
        head = dummy
        while left and right:
            if left.val < right.val:
                dummy.next = ListNode(left.val)
                left = left.next
            else:
                dummy.next = ListNode(right.val)
                right = right.next
            dummy = dummy.next
        # if there is leftover from either list
        if left:
            dummy.next = left
        if right:
            dummy.next = right
        
        return head.next


    # slow and fast pointer helper to get mid in O(logn) time
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
