# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_element = None
        current_element = head

        while current_element:
            next_element = current_element.next
            
            current_element.next = previous_element
            
            previous_element = current_element

            current_element = next_element
        return previous_element
        
