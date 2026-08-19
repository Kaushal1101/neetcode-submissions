# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add_numbers(a, b, carry):
            num_sum = a + b + carry
            new_carry = 0
            if num_sum > 9:
                while num_sum > 9:
                    num_sum -= 10
                    new_carry += 1
            return (num_sum, new_carry)
        
        root = ListNode()
        head = root
        carry = 0

        while l1 and l2:
            num_sum, carry = add_numbers(l1.val, l2.val, carry)
            head.next = ListNode(num_sum)
            head = head.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            num_sum, carry = add_numbers(l1.val, 0, carry)
            head.next = ListNode(num_sum)
            head = head.next
            l1 = l1.next
        
        while l2:
            num_sum, carry = add_numbers(l2.val, 0, carry)
            head.next = ListNode(num_sum)
            head = head.next
            l2 = l2.next
            

        if carry:
            head.next = ListNode(carry)

        return root.next

                