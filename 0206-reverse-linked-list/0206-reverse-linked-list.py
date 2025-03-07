class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None   # The new "end" of the train
        curr = head   # Start at the engine (first car)
        
        while curr:   # While there are train cars left to process
            next_temp = curr.next  # Remember the next car
            curr.next = prev       # Reverse the direction
            prev = curr            # Move the "reversed train" forward
            curr = next_temp       # Move to the next car
        
        return prev  # New head of the reversed train