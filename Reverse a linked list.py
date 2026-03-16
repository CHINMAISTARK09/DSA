## You are given the head of a singly linked list. You have to reverse the linked list and return the head of the reversed list.

class Solution:
    def reverseList(self, head):
        curr=head
        prev=None
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev


Time Complexity O(N) Space Complexity O(1)
