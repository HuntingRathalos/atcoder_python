# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ans = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                ans.next = l1
                l1 = l1.next
            else:
                ans.next = l2
                l2 = l2.next
            ans = ans.next
        ans.next = l1 or l2
        return temp.next
