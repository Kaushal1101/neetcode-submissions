# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle of the linked list
        mid = head
        fast = head
        length = 0

        while fast.next:
            if length % 2 == 0:
                mid = mid.next
            fast = fast.next
            length += 1

        curr = mid.next
        prev = mid
        mid.next = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        p1, p2 = head, prev
        root = ListNode()
        first = True

        while p1 and p2:
            if first:
                root.next = p1
                p1 = p1.next
                first = False
            else:
                root.next = p2
                p2 = p2.next
                first = True
            root = root.next
        
        return root.next


        # Flip the second half
        # Merge two halves
