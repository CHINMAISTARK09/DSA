## Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.

## Note: Internally, pos(1 based index) is used to denote the position of the node that tail's next pointer is connected to. If pos = 0, it means the last node points to null, indicating there is no loop. Note that pos is not passed as a parameter.1

class Solution:
    def lengthOfLoop(self, head):
        if head is None:
            return 0
        slow=head
        fast=head
        count=0
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                count=1
                curr=slow.next
                while curr!=slow:
                    count+=1
                    curr=curr.next
                return count
        return 0         

Time Complexity: O(n) Auxiliary Space: O(1)
