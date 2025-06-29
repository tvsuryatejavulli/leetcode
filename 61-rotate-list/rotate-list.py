class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # If the list is empty or has just one element, no rotation is needed
        if head is None or head.next is None:
            return head
      
        # Count the number of elements in the linked list
        current, length = head, 0
        while current:
            length += 1
            current = current.next

        # Compute the actual number of rotations needed as k could be larger than the length of the list
        k %= length
        if k == 0:  # If no rotation is needed
            return head

        # Use two pointers, fast and slow. Start both at the beginning of the list
        fast = slow = head
      
        # Move the fast pointer k steps ahead
        for _ in range(k):
            fast = fast.next
      
        # Move both pointers at the same speed until fast reaches the end of the list
        while fast.next:
            fast, slow = fast.next, slow.next
      
        # At this point, slow is at the node before the new head after rotation
        # We can now adjust the pointers to complete the rotation
        new_head = slow.next
        slow.next = None  # The next pointer of the new tail should point to None
        fast.next = head  # The next pointer of the old tail should point to the old head
      
        return new_head  # Return the new head of the list

# Note: The Optional[ListNode] type hint should be imported from typing 
# if you want to use it for type checking in Python 3.
# Otherwise, you can omit it from the function signatures.
