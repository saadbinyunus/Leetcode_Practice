# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Two Pointers!
        # input is head (start of the linked list)
        current  = head
        previous = None #none is basically null

        while current != None:
            #We must save the next node before breaking the chain
            next_node = current.next

            #reversing the link
            current.next = previous

            #Moving the pointers ahead
            previous = current
            current = next_node
            
        return previous