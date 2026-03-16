## You are given the head of a singly linked list. You have to determine whether the given linked list contains a loop or not. A loop exists in a linked list if the next pointer of the last node points to any other node in the list (including itself), rather than being null.

## Note: Internally, pos(1 based index) is used to denote the position of the node that tail's next pointer is connected to. If pos = 0, it means the last node points to null. Note that pos is not passed as a parameter.

class Solution:
    def detectLoop(self, head):
         slow=head
         fast=head
         
         while fast and fast.next:
             slow=slow.next
             fast=fast.next.next
             if slow==fast:
                 return True
         return False

Time Complexity: O(n) Auxiliary Space: O(1)
