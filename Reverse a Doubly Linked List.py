## You are given the head of a doubly linked list. You have to reverse the doubly linked list and return its head.

class Solution:
    def reverse(self, head):
        if head is None:
            return head
        curr=head
        new_head=None  --- Just to store the new head
        while curr:
            curr.next,curr.prev=curr.prev,curr.next
            new_head=curr  -- if we dont store this, in the last iteration curr will become None, so we cant return None
            curr=curr.prev
        return new_head

#Time Complexity: O(n) Auxiliary Space: O(1)
