# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        n2 = 0
        curr = head

        while curr!=None:
            arr.append(curr)
            curr=curr.next
        
        arr.pop(-n)

        for i in range(len(arr)-1):
            arr[i].next = arr[i+1]
        
        if arr:
            arr[-1].next=None
            return arr[0]
        
        